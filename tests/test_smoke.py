def test_package_dependency():
    """Prueba si el paquete 'pandas' está disponible en el entorno."""
    try:
        import pandas
    except ImportError:
        print("Pandas no está instalado en el entorno de pruebas.")

    assert pandas.__version__ is not None
