"""
📊 DATA PIPELINE SIMPLE - Workshop Trading Algorítmico

Script básico pero profesional para descargar, limpiar y validar datos históricos
de mercado usando yfinance (gratis y sin API key).

Características:
- ✅ Descarga datos de acciones/ETFs/criptos
- ✅ Limpia datos (elimina NaN, duplicados, gaps)
- ✅ Valida calidad de datos
- ✅ Guarda en CSV para reutilización
- ✅ Maneja errores comunes

Autor: Workshop Trading Algorítmico Aumentado con IA Generativa
Versión: 1.0 (Público)
Fecha: 20 de noviembre de 2025
"""

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')  # Silenciar warnings de yfinance

# ═════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═════════════════════════════════════════════════════════════════════════════

class DataConfig:
    """Configuración centralizada del pipeline de datos"""
    
    # Tickers a descargar (ejemplos)
    TICKERS = ['SPY', 'QQQ', 'TLT']  # ETFs populares
    
    # Rango de fechas
    START_DATE = '2020-01-01'
    END_DATE = datetime.now().strftime('%Y-%m-%d')  # Hasta hoy
    
    # Timeframe
    INTERVAL = '1d'  # Opciones: 1m, 5m, 15m, 1h, 1d, 1wk, 1mo
    
    # Output
    OUTPUT_DIR = './data/'  # Carpeta donde guardar CSVs
    
    # Validación
    MIN_DATA_POINTS = 100  # Mínimo de días para considerar dataset válido
    MAX_NAN_PERCENT = 5.0  # % máximo de NaN aceptable


# ═════════════════════════════════════════════════════════════════════════════
# FUNCIONES PRINCIPALES
# ═════════════════════════════════════════════════════════════════════════════

def download_data(ticker: str, start_date: str, end_date: str, 
                  interval: str = '1d') -> pd.DataFrame:
    """
    Descarga datos históricos de un ticker usando yfinance.
    
    Args:
        ticker: Símbolo del activo (ej: 'SPY', 'AAPL', 'BTC-USD')
        start_date: Fecha inicio en formato 'YYYY-MM-DD'
        end_date: Fecha fin en formato 'YYYY-MM-DD'
        interval: Timeframe ('1d', '1h', etc.)
    
    Returns:
        DataFrame con columnas OHLCV
    
    Raises:
        ValueError: Si no se pueden descargar datos
    """
    print(f"📥 Descargando {ticker} desde {start_date} hasta {end_date}...")
    
    try:
        # Descargar usando yfinance
        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            interval=interval,
            progress=False,  # Silenciar barra de progreso
            auto_adjust=True  # Ajustar por splits y dividendos
        )
        
        # Validar que se descargaron datos
        if df.empty:
            raise ValueError(f"No se encontraron datos para {ticker}")
        
        # Normalizar nombres de columnas (yfinance puede retornar con mayúsculas)
        df.columns = [col.lower() for col in df.columns]
        
        print(f"✅ Descargados {len(df)} registros de {ticker}")
        return df
        
    except Exception as e:
        print(f"❌ Error descargando {ticker}: {str(e)}")
        raise ValueError(f"No se pudo descargar {ticker}")


def clean_data(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """
    Limpia datos eliminando NaN, duplicados, y validando estructura.
    
    Args:
        df: DataFrame con datos descargados
        ticker: Nombre del ticker (para logging)
    
    Returns:
        DataFrame limpio
    """
    print(f"🧹 Limpiando datos de {ticker}...")
    
    # Guardar tamaño original para reporte
    original_len = len(df)
    
    # 1. Eliminar duplicados en el índice (fechas duplicadas)
    df = df[~df.index.duplicated(keep='first')]
    duplicates_removed = original_len - len(df)
    if duplicates_removed > 0:
        print(f"   ⚠️  Eliminados {duplicates_removed} registros duplicados")
    
    # 2. Verificar columnas requeridas
    required_cols = ['open', 'high', 'low', 'close', 'volume']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Faltan columnas requeridas: {missing_cols}")
    
    # 3. Convertir columnas a tipo numérico (por si acaso)
    for col in required_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # 4. Eliminar filas donde TODAS las columnas son NaN
    df = df.dropna(how='all')
    
    # 5. Para datos faltantes parciales, hacer forward fill (máx 2 días)
    # Rationale: Gaps de 1-2 días son normales (fines de semana, feriados)
    nan_before = df.isnull().sum().sum()
    df = df.fillna(method='ffill', limit=2)
    nan_after = df.isnull().sum().sum()
    
    if nan_before > 0:
        print(f"   ⚠️  Rellenados {nan_before - nan_after} valores NaN con forward fill")
    
    # 6. Si aún quedan NaN después de ffill, eliminar esas filas
    rows_before = len(df)
    df = df.dropna()
    rows_dropped = rows_before - len(df)
    
    if rows_dropped > 0:
        print(f"   ⚠️  Eliminadas {rows_dropped} filas con NaN persistentes")
    
    # 7. Validar lógica OHLC (High >= Low, etc.)
    invalid_ohlc = df[
        (df['high'] < df['low']) | 
        (df['close'] > df['high']) | 
        (df['close'] < df['low'])
    ]
    
    if len(invalid_ohlc) > 0:
        print(f"   ⚠️  Encontradas {len(invalid_ohlc)} filas con OHLC inválido (eliminadas)")
        df = df.drop(invalid_ohlc.index)
    
    # 8. Eliminar filas con precio = 0 (datos corruptos)
    zero_prices = df[(df['close'] == 0) | (df['high'] == 0)]
    if len(zero_prices) > 0:
        print(f"   ⚠️  Eliminadas {len(zero_prices)} filas con precio = 0")
        df = df.drop(zero_prices.index)
    
    print(f"✅ Limpieza completada: {len(df)} registros válidos ({original_len - len(df)} eliminados)")
    return df


def validate_data(df: pd.DataFrame, ticker: str, 
                  min_points: int = 100, 
                  max_nan_percent: float = 5.0) -> dict:
    """
    Valida calidad de datos y genera reporte.
    
    Args:
        df: DataFrame limpio
        ticker: Nombre del ticker
        min_points: Mínimo de registros requeridos
        max_nan_percent: % máximo de NaN aceptable
    
    Returns:
        dict con estadísticas de validación
    """
    print(f"✅ Validando calidad de datos de {ticker}...")
    
    # Inicializar reporte
    report = {
        'ticker': ticker,
        'total_records': len(df),
        'date_range': f"{df.index.min()} to {df.index.max()}",
        'is_valid': True,
        'errors': [],
        'warnings': []
    }
    
    # Validación 1: Cantidad mínima de datos
    if len(df) < min_points:
        report['is_valid'] = False
        report['errors'].append(
            f"Muy pocos datos: {len(df)} < {min_points} requeridos"
        )
    
    # Validación 2: Porcentaje de NaN
    nan_percent = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
    if nan_percent > max_nan_percent:
        report['is_valid'] = False
        report['errors'].append(
            f"Demasiados NaN: {nan_percent:.2f}% > {max_nan_percent}% límite"
        )
    
    # Validación 3: Gaps grandes en fechas (solo para datos diarios)
    if '1d' in str(df.index.freq) or df.index.freq is None:
        date_diff = df.index.to_series().diff()
        # Gaps >10 días son sospechosos (excluyendo inicio)
        large_gaps = date_diff[date_diff > timedelta(days=10)].iloc[1:]
        
        if len(large_gaps) > 0:
            report['warnings'].append(
                f"Detectados {len(large_gaps)} gaps >10 días en fechas"
            )
    
    # Validación 4: Volatilidad extrema (posible dato corrupto)
    returns = df['close'].pct_change()
    extreme_returns = returns[abs(returns) > 0.5]  # >50% cambio en 1 día
    
    if len(extreme_returns) > 0:
        report['warnings'].append(
            f"Detectados {len(extreme_returns)} cambios de precio >50% (revisar)"
        )
    
    # Estadísticas adicionales
    report['stats'] = {
        'avg_volume': f"{df['volume'].mean():,.0f}",
        'avg_price': f"${df['close'].mean():.2f}",
        'price_range': f"${df['close'].min():.2f} - ${df['close'].max():.2f}",
        'nan_count': int(df.isnull().sum().sum())
    }
    
    # Imprimir resultado
    if report['is_valid']:
        print(f"   ✅ Validación EXITOSA")
    else:
        print(f"   ❌ Validación FALLIDA:")
        for error in report['errors']:
            print(f"      - {error}")
    
    if report['warnings']:
        print(f"   ⚠️  Advertencias:")
        for warning in report['warnings']:
            print(f"      - {warning}")
    
    return report


def save_to_csv(df: pd.DataFrame, ticker: str, output_dir: str = './data/'):
    """
    Guarda DataFrame a CSV para reutilización.
    
    Args:
        df: DataFrame a guardar
        ticker: Nombre del ticker
        output_dir: Directorio de salida
    """
    import os
    
    # Crear directorio si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    # Generar nombre de archivo
    filename = f"{ticker}_{datetime.now().strftime('%Y%m%d')}.csv"
    filepath = os.path.join(output_dir, filename)
    
    # Guardar
    df.to_csv(filepath)
    print(f"💾 Guardado en: {filepath}")


# ═════════════════════════════════════════════════════════════════════════════
# PIPELINE COMPLETO
# ═════════════════════════════════════════════════════════════════════════════

def run_pipeline(tickers: list, start_date: str, end_date: str, 
                 interval: str = '1d', output_dir: str = './data/') -> dict:
    """
    Ejecuta pipeline completo para múltiples tickers.
    
    Args:
        tickers: Lista de tickers a procesar
        start_date: Fecha inicio
        end_date: Fecha fin
        interval: Timeframe
        output_dir: Directorio de salida
    
    Returns:
        dict con resultados por ticker
    """
    print("\n" + "="*80)
    print("🚀 INICIANDO DATA PIPELINE")
    print("="*80 + "\n")
    
    results = {}
    
    for ticker in tickers:
        print(f"\n{'─'*80}")
        print(f"Procesando: {ticker}")
        print(f"{'─'*80}")
        
        try:
            # 1. Descargar
            df = download_data(ticker, start_date, end_date, interval)
            
            # 2. Limpiar
            df = clean_data(df, ticker)
            
            # 3. Validar
            validation = validate_data(
                df, ticker, 
                min_points=DataConfig.MIN_DATA_POINTS,
                max_nan_percent=DataConfig.MAX_NAN_PERCENT
            )
            
            # 4. Guardar si es válido
            if validation['is_valid']:
                save_to_csv(df, ticker, output_dir)
                results[ticker] = {
                    'status': 'success',
                    'data': df,
                    'validation': validation
                }
            else:
                results[ticker] = {
                    'status': 'failed_validation',
                    'validation': validation
                }
            
        except Exception as e:
            print(f"❌ Error procesando {ticker}: {str(e)}")
            results[ticker] = {
                'status': 'error',
                'error': str(e)
            }
    
    # Reporte final
    print("\n" + "="*80)
    print("📊 RESUMEN FINAL")
    print("="*80)
    
    success = sum(1 for r in results.values() if r['status'] == 'success')
    failed = len(results) - success
    
    print(f"✅ Exitosos: {success}/{len(results)}")
    print(f"❌ Fallidos: {failed}/{len(results)}")
    
    return results


# ═════════════════════════════════════════════════════════════════════════════
# EJEMPLO DE USO
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    """
    Ejemplo de cómo usar este script.
    """
    
    # Opción 1: Usar configuración por defecto
    results = run_pipeline(
        tickers=DataConfig.TICKERS,
        start_date=DataConfig.START_DATE,
        end_date=DataConfig.END_DATE,
        interval=DataConfig.INTERVAL,
        output_dir=DataConfig.OUTPUT_DIR
    )
    
    # Opción 2: Personalizar parámetros
    # results = run_pipeline(
    #     tickers=['AAPL', 'MSFT', 'GOOGL'],
    #     start_date='2023-01-01',
    #     end_date='2024-01-01',
    #     interval='1h',  # Datos horarios
    #     output_dir='./mi_carpeta_datos/'
    # )
    
    # Acceder a datos de un ticker específico
    if 'SPY' in results and results['SPY']['status'] == 'success':
        spy_data = results['SPY']['data']
        print(f"\n📈 Primeras 5 filas de SPY:")
        print(spy_data.head())
        
        print(f"\n📊 Estadísticas de SPY:")
        print(spy_data.describe())


# ═════════════════════════════════════════════════════════════════════════════
# NOTAS PARA EL USUARIO
# ═════════════════════════════════════════════════════════════════════════════

"""
📚 GUÍA DE USO RÁPIDO:

1. INSTALACIÓN DE DEPENDENCIAS:
   pip install yfinance pandas numpy

2. EJECUCIÓN BÁSICA:
   python data_pipeline_simple.py

3. PERSONALIZACIÓN:
   - Edita la clase DataConfig para cambiar tickers/fechas
   - O llama a run_pipeline() con tus propios parámetros

4. OUTPUT:
   - CSVs guardados en ./data/ por defecto
   - Formato: TICKER_YYYYMMDD.csv

5. TIMEFRAMES DISPONIBLES:
   - Intraday: '1m', '5m', '15m', '30m', '1h'
   - Daily y más: '1d', '1wk', '1mo'

⚠️ LIMITACIONES DE YFINANCE:
   - Datos intraday: Máximo 60 días de historial
   - Datos diarios: Sin límite (años disponibles)
   - Criptos: Usar formato 'BTC-USD', 'ETH-USD'
   - Forex: Usar formato 'EURUSD=X'

🎓 SIGUIENTE PASO:
   Usa estos datos limpios en tu backtest (Sesión 5 del workshop)

🔗 EN EL WORKSHOP PREMIUM:
   - data_pipeline_advanced.py (con caching, multi-threading)
   - Integración con Alpaca, Interactive Brokers, Polygon
   - Auto-detección de splits/dividendos
   - Normalización multi-fuente (combinar yfinance + Alpaca)
"""
