# ============================================================
# 📥 DESCARGAR DATOS - VERSIÓN PROFESIONAL CON VALIDACIÓN
# ============================================================

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta
import pandas as pd

def descargar_datos_alpaca(
    simbolo: str,
    api_key: str,
    secret_key: str,
    start_date: datetime = None,
    end_date: datetime = None,
    timeframe = TimeFrame.Day
) -> pd.DataFrame:
    """
    Descarga datos históricos de Alpaca con manejo robusto de errores.
    
    🎓 TEORÍA (López de Prado, 2018):
    "La calidad del backtesting depende de la calidad de los datos.
     Validar fechas ANTES de solicitar datos evita errores silenciosos."
    
    Args:
        simbolo: Ticker del activo (ej: "SPY", "AAPL")
        api_key: API Key de Alpaca
        secret_key: Secret Key de Alpaca
        start_date: Fecha inicio (default: 5 años atrás)
        end_date: Fecha fin (default: ayer)
        timeframe: Resolución temporal (Day, Hour, Minute)
    
    Returns:
        DataFrame con columnas: open, high, low, close, volume
    
    Raises:
        ValueError: Si las fechas son inválidas
        APIError: Si hay problemas con las credenciales o permisos
    """
    
    print(f"📥 Descargando datos de {simbolo}...")
    print("=" * 60)
    
    # ============================================================
    # VALIDACIÓN 1: Fechas por defecto si no se proveen
    # ============================================================
    
    if end_date is None:
        # ⚠️ CRÍTICO: Plan gratuito requiere al menos 1 día de antigüedad
        end_date = datetime.now() - timedelta(days=1)
        print(f"⏰ Fecha fin no especificada. Usando: {end_date.date()} (ayer)")
    
    if start_date is None:
        start_date = end_date - timedelta(days=365*5)  # 5 años por defecto
        print(f"📅 Fecha inicio no especificada. Usando: {start_date.date()} (5 años atrás)")
    
    # ============================================================
    # VALIDACIÓN 2: Verificar restricción de 15 minutos
    # ============================================================
    
    ahora = datetime.now()
    diferencia_minutos = (ahora - end_date).total_seconds() / 60
    
    if diferencia_minutos < 15:
        print("\n⚠️ ADVERTENCIA: Restricción de plan gratuito detectada")
        print(f"   Intentas datos de hace {diferencia_minutos:.0f} minutos")
        print(f"   Plan gratuito requiere al menos 15 minutos de antigüedad")
        print(f"   Ajustando automáticamente a: {(ahora - timedelta(minutes=20)).date()}")
        end_date = ahora - timedelta(minutes=20)  # 20 min para estar seguros
    
    # ============================================================
    # VALIDACIÓN 3: Verificar orden cronológico
    # ============================================================
    
    if start_date >= end_date:
        raise ValueError(
            f"❌ Error: start_date ({start_date}) debe ser anterior a end_date ({end_date})"
        )
    
    # ============================================================
    # DESCARGA CON MANEJO DE ERRORES
    # ============================================================
    
    try:
        # Crear cliente
        data_client = StockHistoricalDataClient(api_key, secret_key)
        
        # Crear request
        request_params = StockBarsRequest(
            symbol_or_symbols=[simbolo],
            timeframe=timeframe,
            start=start_date,
            end=end_date
        )
        
        # Ejecutar descarga
        print(f"\n🔄 Solicitando datos a Alpaca...")
        bars = data_client.get_stock_bars(request_params)
        
        # Convertir a DataFrame
        df = bars.df
        
        # ============================================================
        # VALIDACIÓN 4: Verificar calidad de datos
        # ============================================================
        
        if df.empty:
            raise ValueError(
                f"❌ No se encontraron datos para {simbolo} en el período especificado"
            )
        
        # Verificar valores nulos
        nulos_por_columna = df.isnull().sum()
        if nulos_por_columna.any():
            print(f"\n⚠️ Advertencia: Datos con valores nulos detectados:")
            print(nulos_por_columna[nulos_por_columna > 0])
        
        # Verificar gaps de fechas (días faltantes sospechosos)
        dias_unicos = len(df.index.unique())
        dias_esperados = (end_date - start_date).days
        porcentaje_cobertura = (dias_unicos / dias_esperados) * 100
        
        if porcentaje_cobertura < 50:  # Menos del 50% de días esperados
            print(f"\n⚠️ Advertencia: Cobertura de datos baja ({porcentaje_cobertura:.1f}%)")
            print(f"   Días con datos: {dias_unicos} / {dias_esperados} esperados")
        
        # ============================================================
        # RESUMEN DE DESCARGA
        # ============================================================
        
        print(f"\n✅ Descarga completada exitosamente")
        print("=" * 60)
        print(f"📊 Símbolo: {simbolo}")
        print(f"📅 Período: {df.index[0].date()} a {df.index[-1].date()}")
        print(f"📈 Total de registros: {len(df)}")
        print(f"📊 Resolución: {timeframe}")
        print(f"💰 Precio más reciente: ${df['close'].iloc[-1]:.2f}")
        print(f"📉 Precio más antiguo: ${df['close'].iloc[0]:.2f}")
        print(f"📈 Retorno total: {((df['close'].iloc[-1] / df['close'].iloc[0]) - 1) * 100:.2f}%")
        print("=" * 60)
        
        return df
        
    except Exception as e:
        error_msg = str(e)
        
        # ============================================================
        # DIAGNÓSTICO DE ERRORES COMUNES
        # ============================================================
        
        if "subscription does not permit" in error_msg.lower():
            print(f"\n❌ ERROR: Restricción de suscripción gratuita")
            print(f"   Causa: Intentaste acceder a datos muy recientes (<15 min)")
            print(f"   Solución automática aplicada, pero el servidor rechazó la solicitud")
            print(f"\n🔧 Solución manual:")
            print(f"   1. Ajusta end_date a al menos 1 día atrás:")
            print(f"      end_date = datetime.now() - timedelta(days=1)")
            print(f"   2. O considera actualizar a Algo Trader Plus ($99/mes)")
        
        elif "invalid credentials" in error_msg.lower():
            print(f"\n❌ ERROR: Credenciales inválidas")
            print(f"   Verifica que API_KEY y SECRET_KEY sean correctos")
            print(f"   Revisa el archivo alpaca_keys.txt en tu escritorio")
        
        elif "connection" in error_msg.lower() or "timeout" in error_msg.lower():
            print(f"\n❌ ERROR: Problema de conexión")
            print(f"   Verifica tu conexión a internet")
            print(f"   Intenta ejecutar la celda nuevamente en 30 segundos")
        
        else:
            print(f"\n❌ ERROR DESCONOCIDO:")
            print(f"   {error_msg}")
            print(f"\n📞 Contacta al instructor si persiste")
        
        raise  # Re-lanzar el error para que el usuario lo vea

# ============================================================
# EJEMPLO DE USO
# ============================================================

# Ejemplo básico (usa valores por defecto inteligentes)
df_spy = descargar_datos_alpaca(
    simbolo="SPY",
    api_key=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY
)

# Ejemplo avanzado (fechas personalizadas)
df_aapl = descargar_datos_alpaca(
    simbolo="AAPL",
    api_key=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY,
    start_date=datetime(2020, 1, 1),
    end_date=datetime.now() - timedelta(days=2),  # Hace 2 días para estar seguros
    timeframe=TimeFrame.Hour  # Datos por hora (no diarios)
)