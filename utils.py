def validar_dato(dato, tipo):
    if not isinstance(dato, str):
        return False
    if tipo == "numero":
        return dato.isdigit()
    elif tipo == "correo":
        return "@" in dato and "." in dato and len(dato.split("@")) == 2
    elif tipo == "texto":
        return dato.isalpha()
    return False

if __name__ == "__main__":
    import unittest
    
    class TestValidarDato(unittest.TestCase):
        def test_validar_numero(self):
            self.assertTrue(validar_dato("123", "numero"))
            self.assertFalse(validar_dato("abc", "numero"))
        
        def test_validar_correo(self):
            self.assertTrue(validar_dato("correo@example.com", "correo"))
            self.assertFalse(validar_dato("correo@com", "correo"))
        
        def test_validar_texto(self):
            self.assertTrue(validar_dato("Hola", "texto"))
            self.assertFalse(validar_dato("Hola123", "texto"))
    
    unittest.main()
