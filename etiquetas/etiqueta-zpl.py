
def criar_etiqueta(id_produto):
    zpl = '''^XA
        ^CF0,30
        ^FO50,50^GB700,1100,3^FS
        ^FO50,50^FDProduto: ^FS
        ^FO50,100^FDCodigo de Barras: 123456789^FS
        ^FO50,150^FDTipo: Carne^FS
        ^FO50,200^FDCorte: Picanha^FS
        ^FO50,250^FDSexo: Masculino^FS
        ^FO50,300^FDFabricacao: 17-04-2024^FS
        ^FO50,350^FDValidade: 17-04-2024^FS
        ^FO50,400^FDSIF: sif^FS
        ^FO50,450^FDLote: lote^FS

        ^FO50,500^GB700,1,3^FS

        ^FO50,550^FDInformacoes Nutricionais:^FS
        ^FO50,600^GB700,1,3^FS
        ^FO50,650^FDPorcoes por embalagem: 1^FS
        ^FO50,700^FDPorcao: 100g^FS

        ^FO50,750^GB700,1,3^FS

        ^FO50,800^FDValor Energetico (kcal): 250^FS
        ^FO50,850^FDCarboidratos totais (g): 30^FS
        ^FO50,900^FDAcucares totais (g): 20^FS
        ^FO50,950^FDAcucares adicionados (g): 10^FS
        ^FO50,1000^FDProteinas (g): 15^FS
        ^FO50,1050^FDGorduras totais (g): 10^FS
        ^FO50,1100^FDGorduras saturadas (g): 5^FS
        ^FO50,1150^FDGorduras trans (g): 0^FS
        ^FO50,1200^FDFibra alimentar (g): 5^FS
        ^FO50,1250^FDSodio (mg): 500^FS
        ^XZ'''
        
    return zpl
