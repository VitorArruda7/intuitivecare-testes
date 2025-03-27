import unittest
import pandas as pd
import zipfile
import os
from data_transformation.transform import limpar_texto, extrair_tabela_pdf, abreviacoes

class TestTransformacaoDados(unittest.TestCase):
    
    def test_limpar_texto(self):
        """Testa a limpeza de texto para remoção de espaços extras e normalização de valores nulos"""
        self.assertEqual(limpar_texto("  Teste   de Texto   "), "Teste de Texto")
        self.assertEqual(limpar_texto(None), "")
        self.assertEqual(limpar_texto(""), "")
        self.assertEqual(limpar_texto("   "), "")
        self.assertEqual(limpar_texto("Texto\ncom\nquebras"), "Texto com quebras")
    
    def test_substituicao_abreviacoes(self):
        """Testa a substituição das abreviações OD e AMB"""
        df = pd.DataFrame({"OD": ["OD", ""], "AMB": ["AMB", ""]})
        df["OD"] = df["OD"].replace(abreviacoes)
        df["AMB"] = df["AMB"].replace(abreviacoes)
        self.assertEqual(df.loc[0, "OD"], "Seg. Odontológica")
        self.assertEqual(df.loc[0, "AMB"], "Seg. Ambulatorial")
        self.assertEqual(df.loc[1, "OD"], "")
        self.assertEqual(df.loc[1, "AMB"], "")
    
    def test_geracao_csv_zip(self):
        """Testa se o CSV e o ZIP são gerados corretamente"""
        df = pd.DataFrame({"Coluna1": ["Dado1", "Dado2"], "Coluna2": ["Info1", "Info2"]})
        output_csv = "teste_transform.csv"
        output_zip = "teste_transform.zip"
        
        df.to_csv(output_csv, index=False, encoding="utf-8-sig", sep=";")
        with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(output_csv)
        
        self.assertTrue(os.path.exists(output_csv))
        self.assertTrue(os.path.exists(output_zip))
        
        os.remove(output_csv)
        os.remove(output_zip)
    
if __name__ == "__main__":
    unittest.main()
