
from pandas_datareader import data as pdr
import pandas as pd
import yfinance as yf
import indicators as ind
import ta
from trading_ig import IGService
from joblib import dump, load

yf.pdr_override()

# We take all the cotation from start of cotation until 10/17/2020.
start_date = '2010-01-03'

# end_date = '2020-03-03'
end_date = '2022-05-13'

cac40 = yf.Ticker("^FCHI").history(start=start_date,
                                   end=end_date)  # pdr.get_data_yahoo('^FCHI', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
cac40["Adj Close"] = cac40["Close"]

SaintGobain = yf.Ticker('SGO.PA').history(start=start_date,
                                          end=end_date)  # pdr.get_data_yahoo('SGO.PA', start = start_date, end = end_date)# data.DataReader('SGO.PA', 'yahoo', start_date, end_date)
SaintGobain["Adj Close"] = SaintGobain["Close"]

Total = yf.Ticker('TTE.PA').history(start=start_date,
                                    end=end_date)  # pdr.get_data_yahoo('FP.PA', start = start_date, end = end_date)#data.DataReader('FP.PA', 'yahoo', start_date, end_date)
Total["Adj Close"] = Total["Close"]

SociétéGénérale = yf.Ticker("GLE.PA").history(start=start_date,
                                              end=end_date)  # pdr.get_data_yahoo('GLE.PA', start = start_date, end = end_date)# data.DataReader('GLE.PA', 'yahoo', start_date, end_date)
SociétéGénérale["Adj Close"] = SociétéGénérale["Close"]

Worldline = yf.Ticker('WLN.PA').history(start=start_date,
                                        end=end_date)  # pdr.get_data_yahoo('WLN.PA', start = start_date, end = end_date)# data.DataReader('WLN.PA', 'yahoo', start_date, end_date)
Worldline["Adj Close"] = Worldline["Close"]

Michelin = yf.Ticker("ML.PA").history(start=start_date,
                                      end=end_date)  # pdr.get_data_yahoo('ML.PA', start = start_date, end = end_date)# data.DataReader('ML.PA', 'yahoo', start_date, end_date)
Michelin["Adj Close"] = Michelin["Close"]

Vinci = yf.Ticker("DG.PA").history(start=start_date,
                                   end=end_date)  # pdr.get_data_yahoo('DG.PA', start = start_date, end = end_date)# data.DataReader('DG.PA', 'yahoo', start_date, end_date)
Vinci["Adj Close"] = Vinci["Close"]

BNPParibas = yf.Ticker("BNP.PA").history(start=start_date,
                                         end=end_date)  # pdr.get_data_yahoo('BNP.PA', start = start_date, end = end_date)# data.DataReader('BNP.PA', 'yahoo', start_date, end_date)
BNPParibas["Adj Close"] = BNPParibas["Close"]

CréditAgricole = yf.Ticker('ACA.PA').history(start=start_date,
                                             end=end_date)  # pdr.get_data_yahoo('ACA.PA', start = start_date, end = end_date)# data.DataReader('ACA.PA', 'yahoo', start_date, end_date)
CréditAgricole["Adj Close"] = CréditAgricole["Close"]

Airbus = yf.Ticker("AIR.PA").history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('AIR.PA', start = start_date, end = end_date)# data.DataReader('AIR.PA', 'yahoo', start_date, end_date)
Airbus["Adj Close"] = Airbus["Close"]

Atos = yf.Ticker('ATO.PA').history(start=start_date,
                                   end=end_date)  # pdr.get_data_yahoo('ATO.PA', start = start_date, end = end_date)#data.DataReader('ATO.PA', 'yahoo', start_date, end_date)
Atos["Adj Close"] = Atos["Close"]

SchneiderElectric = yf.Ticker('SU.PA').history(start=start_date,
                                               end=end_date)  # pdr.get_data_yahoo('SU.PA', start = start_date, end = end_date)# data.DataReader('SU.PA', 'yahoo', start_date, end_date)
SchneiderElectric["Adj Close"] = SchneiderElectric["Close"]

Danone = yf.Ticker('BN.PA').history(start=start_date,
                                    end=end_date)  # pdr.get_data_yahoo('BN.PA', start = start_date, end = end_date)#data.DataReader('BN.PA', 'yahoo', start_date, end_date)
Danone["Adj Close"] = Danone["Close"]

Sodexo = yf.Ticker('SW.PA').history(start=start_date,
                                    end=end_date)  # data.DataReader('SW.PA', 'yahoo', start_date, end_date)
Sodexo["Adj Close"] = Sodexo["Close"]

Engie = yf.Ticker('ENGI.PA').history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('ENGI.PA', start = start_date, end = end_date)# data.DataReader('ENGI.PA', 'yahoo', start_date, end_date)
Engie["Adj Close"] = Engie["Close"]

Sanofi = yf.Ticker("SAN.PA").history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo("(SAN.PA", start = start_date, end = end_date)# data.DataReader('SAN.PA', 'yahoo', start_date, end_date)
Sanofi["Adj Close"] = Sanofi["Close"]

VeoliaEnvironnement = yf.Ticker("VIE.PA").history(start=start_date,
                                                  end=end_date)  # pdr.get_data_yahoo(VIE.PA, start = start_date, end = end_date)#data.DataReader('VIE.PA', 'yahoo', start_date, end_date)
VeoliaEnvironnement["Adj Close"] = VeoliaEnvironnement["Close"]
# Peugeot = yf.Ticker('UG.PA').history(start = start_date, end = "2019-01-25")#data.DataReader('UG.PA', 'yahoo', start_date, end_date)
# Peugeot["Adj Close"] = Peugeot["Close"]

Bouygues = yf.Ticker("EN.PA").history(start=start_date,
                                      end=end_date)  # pdr.get_data_yahoo('EN.PA', start = start_date, end = end_date)# data.DataReader('EN.PA', 'yahoo', start_date, end_date)
Bouygues["Adj Close"] = Bouygues["Close"]

Thales = yf.Ticker('HO.PA').history(start=start_date,
                                    end=end_date)  # pdr.get_data_yahoo('HO.PA', start = start_date, end = end_date)#data.DataReader('HO.PA', 'yahoo', start_date, end_date)
Thales["Adj Close"] = Thales["Close"]

Capgemini = yf.Ticker("CAP.PA").history(start=start_date,
                                        end=end_date)  # pdr.get_data_yahoo('CAP.PA', start = start_date, end = end_date)# data.DataReader('CAP.PA', 'yahoo', start_date, end_date)
Capgemini["Adj Close"] = Capgemini["Close"]

Kering = yf.Ticker('KER.PA').history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('KER.PA', start = start_date, end = end_date)#data.DataReader('KER.PA', 'yahoo', start_date, end_date)
Kering["Adj Close"] = Kering["Close"]

Orange = yf.Ticker('ORA.PA').history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('ORA.PA', start = start_date, end = end_date)# data.DataReader('ORA.PA', 'yahoo', start_date, end_date)
Orange["Adj Close"] = Orange["Close"]

Carrefour = yf.Ticker("CA.PA").history(start=start_date,
                                       end=end_date)  # pdr.get_data_yahoo('CA.PA', start = start_date, end = end_date)#data.DataReader('CA.PA', 'yahoo', start_date, end_date)
Carrefour["Adj Close"] = Carrefour["Close"]

AirLiquide = yf.Ticker('AI.PA').history(start=start_date,
                                        end=end_date)  # pdr.get_data_yahoo('AI.PA', start = start_date, end = end_date)# data.DataReader('AI.PA', 'yahoo', start_date, end_date)
AirLiquide["Adj Close"] = AirLiquide["Close"]

Legrand = yf.Ticker('LR.PA').history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('LR.PA', start = start_date, end = end_date)# data.DataReader('LR.PA', 'yahoo', start_date, end_date)
Legrand["Adj Close"] = Legrand["Close"]

Vivendi = yf.Ticker("VIV.PA").history(start=start_date,
                                      end=end_date)  # pdr.get_data_yahoo('VIV.PA', start = start_date, end = end_date)# data.DataReader('VIV.PA', 'yahoo', start_date, end_date)
Vivendi["Adj Close"] = Vivendi["Close"]

PernodRicard = yf.Ticker('RI.PA').history(start=start_date,
                                          end=end_date)  # pdr.get_data_yahoo('RI.PA', start = start_date, end = end_date)# data.DataReader('RI.PA', 'yahoo', start_date, end_date)
PernodRicard["Adj Close"] = PernodRicard["Close"]

Lvmh = yf.Ticker('MC.PA').history(start=start_date,
                                  end=end_date)  # pdr.get_data_yahoo('MC.PA', start = start_date, end = end_date)#data.DataReader('MC.PA', 'yahoo', start_date, end_date)
Lvmh["Adj Close"] = Lvmh["Close"]

Loreal = yf.Ticker('OR.PA').history(start=start_date,
                                    end=end_date)  # pdr.get_data_yahoo('OR.PA', start = start_date, end = end_date)#data.DataReader('OR.PA', 'yahoo', start_date, end_date)
Loreal["Adj Close"] = Loreal["Close"]

Hermes = yf.Ticker('HESAY').history(start=start_date,
                                    end=end_date)  # pdr.get_data_yahoo('HESAY', start = start_date, end = end_date)#data.DataReader('HESAY', 'yahoo', start_date, end_date)
Hermes["Adj Close"] = Hermes["Close"]

Essilor = yf.Ticker('EL.PA').history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('EL.PA', start = start_date, end = end_date)# data.DataReader('EL.PA', 'yahoo', start_date, end_date)
Essilor["Adj Close"] = Essilor["Close"]

Dassault = yf.Ticker('DSY.PA').history(start=start_date,
                                       end=end_date)  # pdr.get_data_yahoo('DSY.PA', start = start_date, end = end_date)# data.DataReader('DSY.PA', 'yahoo', start_date, end_date)
Dassault["Adj Close"] = Dassault["Close"]

AXA = yf.Ticker('CS.PA').history(start=start_date,
                                 end=end_date)  # pdr.get_data_yahoo('CS.PA', start = start_date, end = end_date)# data.DataReader('CS.PA', 'yahoo', start_date, end_date)
AXA["Adj Close"] = AXA["Close"]

Safran = yf.Ticker('SAF.PA').history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('SAF.PA', start = start_date, end = end_date)#data.DataReader('SAF.PA', 'yahoo', start_date, end_date)
Safran["Adj Close"] = Safran["Close"]

Stellantis = yf.Ticker('STLA.PA').history(start=start_date,
                                          end=end_date)  # data.DataReader('STLA.PA', 'yahoo', start_date, end_date)
Stellantis["Adj Close"] = Stellantis["Close"]

Eurofins = yf.Ticker('ERF.PA').history(start=start_date,
                                       end=end_date)  # data.DataReader('STLA.PA', 'yahoo', start_date, end_date)
Eurofins["Adj Close"] = Eurofins["Close"]

Stmicroelectronics = yf.Ticker('STM.PA').history(start=start_date,
                                                 end=end_date)  # pdr.get_data_yahoo('STM.PA', start = start_date, end = end_date)#data.DataReader('STM.PA', 'yahoo', start_date, end_date)
Stmicroelectronics["Adj Close"] = Stmicroelectronics["Close"]

Arcelor = yf.Ticker('MT.AS').history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('MT.AS', start = start_date, end = end_date)# data.DataReader('MT.AS', 'yahoo', start_date, end_date)
Arcelor["Adj Close"] = Arcelor["Close"]

Teleperformance = yf.Ticker('TEP.PA').history(start=start_date,
                                              end=end_date)  # pdr.get_data_yahoo('TEP.PA', start = start_date, end = end_date)#data.DataReader('TEP.PA', 'yahoo', start_date, end_date)
Teleperformance["Adj Close"] = Teleperformance["Close"]

Alstom = yf.Ticker('ALO.PA').history(start=start_date,
                                     end=end_date)  # pdr.get_data_yahoo('ALO.PA', start = start_date, end = end_date)#data.DataReader('ALO.PA', 'yahoo', start_date, end_date)
Alstom["Adj Close"] = Alstom["Close"]

Renault = yf.Ticker('RNO.PA').history(start=start_date,
                                      end=end_date)  # pdr.get_data_yahoo('RNO.PA', start = start_date, end = end_date)# data.DataReader('RNO.PA', 'yahoo', start_date, end_date)
Renault["Adj Close"] = Renault["Close"]

Publicis = yf.Ticker('PUB.PA').history(start=start_date,
                                       end=end_date)  # pdr.get_data_yahoo('PUB.PA', start = start_date, end = end_date)#data.DataReader('PUB.PA', 'yahoo', start_date, end_date)
Publicis["Adj Close"] = Publicis["Close"]

Unibail = yf.Ticker('URW.AS').history(start=start_date,
                                      end=end_date)  # pdr.get_data_yahoo('URW.AS', start = start_date, end = end_date)#data.DataReader('URW.AS', 'yahoo', start_date, end_date)
Unibail["Adj Close"] = Unibail["Close"]

dow = yf.Ticker('^DJI').history(start=start_date,
                                end=end_date)  # pdr.get_data_yahoo('^DJI', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
dow["Adj Close"] = dow["Close"]

snp = yf.Ticker('^GSPC').history(start=start_date,
                                 end=end_date)  # pdr.get_data_yahoo('^GSPC', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
snp["Adj Close"] = snp["Close"]

nasdaq = yf.Ticker('^IXIC').history(start=start_date,
                                    end=end_date)  # pdr.get_data_yahoo('^IXIC', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
nasdaq["Adj Close"] = nasdaq["Close"]

nikkei = yf.Ticker('^N225').history(start=start_date,
                                    end=end_date)  # pdr.get_data_yahoo('^N225', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
nikkei["Adj Close"] = nikkei["Close"]

dax = yf.Ticker('^GDAXI').history(start=start_date,
                                  end=end_date)  # pdr.get_data_yahoo('^GDAXI', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
dax["Adj Close"] = dax["Close"]

ftse = yf.Ticker('^FTSE').history(start=start_date,
                                  end=end_date)  # pdr.get_data_yahoo('^FTSE', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
ftse["Adj Close"] = ftse["Close"]

eur_usd = yf.Ticker('EURUSD=X').history(start=start_date,
                                        end=end_date)  # pdr.get_data_yahoo('EURUSD=X', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
eur_usd["Adj Close"] = eur_usd["Close"]

gold = yf.Ticker('GC=F').history(start=start_date,
                                 end=end_date)  # pdr.get_data_yahoo('GC=F', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
gold["Adj Close"] = gold["Close"]

petrole = yf.Ticker('CL=F').history(start=start_date,
                                    end=end_date)  # pdr.get_data_yahoo('CL=F', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
petrole["Adj Close"] = petrole["Close"]

# cac40["Daily Stock Return"] = ind.dret(cac40)
# cac40 = cac40.dropna()

dow["Daily Stock Return"] = ind.dret(dow)
dow = dow.dropna()

snp["Daily Stock Return"] = ind.dret(snp)
snp = snp.dropna()

nasdaq["Daily Stock Return"] = ind.dret(nasdaq)
nasdaq = nasdaq.dropna()

nikkei["Daily Stock Return"] = ind.dret(nikkei)
nikkei = nikkei.dropna()

dax["Daily Stock Return"] = ind.dret(dax)
dax = dax.dropna()

ftse["Daily Stock Return"] = ind.dret(ftse)
ftse = ftse.dropna()

eur_usd["Daily Stock Return"] = ind.dret(eur_usd)
eur_usd = eur_usd.dropna()

gold["Daily Stock Return"] = ind.dret(gold)
gold = gold.dropna()

petrole["Daily Stock Return"] = ind.dret(petrole)
petrole = petrole.dropna()


class config_ru(object):
    username = "rubentest"
    password = "Stopregarderchien75"
    api_key = "e9802443af7a74ccc0520a6efe6aeb8214aa48fb"
    acc_type = "DEMO"
    acc_number = "Z40TAF"


cup = 1
cdown = 1

ig_service = IGService(config_ru.username, config_ru.password, config_ru.api_key, config_ru.acc_type,
                       acc_number=config_ru.acc_number)
ig_service.create_session()

today = []
df_ind = []
cac40 = yf.Ticker("^FCHI").history(start=start_date,
                                   end=end_date)  # pdr.get_data_yahoo('^FCHI', start = start_date, end = end_date)#data.DataReader('^FCHI', 'yahoo', start_date, end_date)
cac40["Adj Close"] = cac40["Close"]
cac40["Daily Stock Return"] = ind.dret(cac40)
cac40 = cac40.dropna()

cac40['csqt_up'] = ind.csqt_up(cac40)
cac40['csqt_down'] = ind.csqt_down(cac40)
cac40['csq_var'] = ind.csqt_var(cac40)

# cac40 = cac40.drop(cac40.index[0:len(cac40)-len(jpmorgan_df)])

cac40['Var 5j'] = ind.var5j(cac40)
cac40['SMA 100'] = ind.sma(cac40, 100)
cac40['SMA 20'] = ind.sma(cac40, 20)
cac40['SMA 10'] = ind.sma(cac40, 10)

cac40['SMA Change 100'] = ind.sma_change(cac40, 100)
cac40['SMA Change 20'] = ind.sma_change(cac40, 20)
cac40['SMA Change 10'] = ind.sma_change(cac40, 10)
cac40['CAC40 SMA Change 100'] = ind.sma_change(cac40, 100)

cac40['Sharpe Ratio'] = ind.sharpe_ratio(cac40, 1, 63)
cac40['Volatillity'] = ind.volatillity(cac40, 63)
cac40['Cac40 Volatillity'] = ind.volatillity(cac40, 63)
cac40['Beta'] = ind.beta(cac40, cac40, 63)
# today.append(cac40.iloc[-1])
cac40['prediction'] = cac40['Daily Stock Return'].shift(-1)

#

model_sg = ['sg_model1.joblib', 'sg_model1_H.joblib', 'sg_model1_L.joblib']
model_bnp = ['Bnp_model1.joblib', 'Bnp_model1_H.joblib', 'Bnp_model1_L.joblib']
model_airbus = ['Airbus_model1.joblib', 'Airbus_model1_H.joblib', 'Airbus_model1_L.joblib']
model_sanofi = ['sanofi_model1.joblib', 'sanofi_model1_H.joblib', 'sanofi_model1_L.joblib']
model_bouygues = ['Bouygues_model1.joblib', 'Bouygues_model1_H.joblib', 'Bouygues_model1_L.joblib']

model_loreal = ['loreal_model1.joblib', 'loreal_model1_H.joblib', 'loreal_model1_L.joblib']
model_Capgemini = ['Capgemini_model1.joblib', 'Capgemini_model1_H.joblib', 'Capgemini_model1_L.joblib']
model_Dassault = ['Dassault_model1.joblib', 'Dassault_model1_H.joblib', 'Dassault_model1_L.joblib']
model_Carrefour = ['Carrefour_model1.joblib', 'Carrefour_model1_H.joblib', 'Carrefour_model1_L.joblib']

model_Atos = ['Atos_model1.joblib', 'Atos_model1_H.joblib', 'Atos_model1_L.joblib']
model_Engie = ['Engie_model1.joblib', 'Engie_model1_H.joblib', 'Engie_model1_L.joblib']
model_Eurofins = ['Eurofins_model1.joblib', 'Eurofins_model1_H.joblib', 'Eurofins_model1_L.joblib']
model_Renault = ['Renault_model1.joblib', 'Renault_model1_H.joblib', 'Renault_model1_L.joblib']
model_SaintGobain = ['SaintGobain_model1.joblib', 'SaintGobain_model1_H.joblib', 'SaintGobain_model1_L.joblib']
model_Sanofi = ['Sanofi_model1.joblib', 'Sanofi_model1_H.joblib', 'Sanofi_model1_L.joblib']
model_Stmicroelectronics = ['Stmicroelectronics_model1.joblib', 'Stmicroelectronics_model1_H.joblib',
                            'Stmicroelectronics_model1_L.joblib']
model_Thales = ['Thales_model1.joblib', 'Thales_model1_H.joblib', 'Thales_model1_L.joblib']
model_VeoliaEnvironnement = ['VeoliaEnvironnement_model1.joblib', 'VeoliaEnvironnement_model1_H.joblib',
                             'VeoliaEnvironnement_model1_L.joblib']
model_Vinci = ['Vinci_model1.joblib', 'Vinci_model1_H.joblib', 'Vinci_model1_L.joblib']
model_AirLiquide = ['AirLiquide_model1.joblib', 'AirLiquide_model1_H.joblib', 'AirLiquide_model1_L.joblib']
model_Alstom = ['Alstom_model1.joblib', 'Alstom_model1_H.joblib', 'Alstom_model1_L.joblib']
model_Arcelor = ['Arcelor_model1.joblib', 'Arcelor_model1_H.joblib', 'Arcelor_model1_L.joblib']
model_AXA = ['AXA_model1.joblib', 'AXA_model1_H.joblib', 'AXA_model1_L.joblib']
model_CréditAgricole = ['CréditAgricole_model1.joblib', 'CréditAgricole_model1_H.joblib',
                        'CréditAgricole_model1_L.joblib']
model_Danone = ['Danone_model1.joblib', 'Danone_model1_H.joblib', 'Danone_model1_L.joblib']
model_Essilor = ['Essilor_model1.joblib', 'Essilor_model1_H.joblib', 'Essilor_model1_L.joblib']
model_Hermes = ['Hermes_model1.joblib', 'Hermes_model1_H.joblib', 'Hermes_model1_L.joblib']
model_Kering = ['Kering_model1.joblib', 'Kering_model1_H.joblib', 'Kering_model1_L.joblib']
model_Legrand = ['Legrand_model1.joblib', 'Legrand_model1_H.joblib', 'Legrand_model1_L.joblib']
model_Loreal = ['Loreal_model1.joblib', 'Loreal_model1_H.joblib', 'Loreal_model1_L.joblib']
model_LVMH = ['LVMH_model1.joblib', 'LVMH_model1_H.joblib', 'LVMH_model1_L.joblib']
model_Michelin = ['Michelin_model1.joblib', 'Michelin_model1_H.joblib', 'Michelin_model1_L.joblib']
model_Orange = ['Orange_model1.joblib', 'Orange_model1_H.joblib', 'Orange_model1_L.joblib']

model_Worldline = ['Worldline_model1.joblib', 'Worldline_model1_H.joblib', 'Worldline_model1_L.joblib']
model_PernodRicard = ['PernodRicard_model1.joblib', 'PernodRicard_model1_H.joblib',
                      'PernodRicard_model1_L.joblib']
model_Publicis = ['Publicis_model1.joblib', 'Publicis_model1_H.joblib', 'Publicis_model1_L.joblib']
model_Safran = ['Safran_model1.joblib', 'Safran_model1_H.joblib', 'Safran_model1_L.joblib']
model_SchneiderElectric = ['SchneiderElectric_model1.joblib', 'SchneiderElectric_model1_H.joblib',
                           'SchneiderElectric_model1_L.joblib']
model_Sodexo = ['Sodexo_model1.joblib', 'Sodexo_model1_H.joblib', 'Sodexo_model1_L.joblib']
model_Stellantis = ['Stellantis_model1.joblib', 'Stellantis_model1_H.joblib', 'Stellantis_model1_L.joblib']
model_Teleperformance = ['Teleperformance_model1.joblib', 'Teleperformance_model1_H.joblib',
                         'Teleperformance_model1_L.joblib']
model_Total = ['Total_model1.joblib', 'Total_model1_H.joblib', 'Total_model1_L.joblib']
model_Vivendi = ['Vivendi_model1.joblib', 'Vivendi_model1_H.joblib', 'Vivendi_model1_L.joblib']
model_Unibail = [r'Unibail_model1.joblib', r'Unibail_model1_H.joblib', r'Unibail_model1_L.joblib']

model_cac40 = ['cac40_model1.joblib', 'cac40_model1_H.joblib', 'cac40_model1_L.joblib']

i = 0
#          (AirLiquide, "Air Liquide", model_AirLiquide, "EC.D.AI.CASH.IP"),

lscac = [
    (AirLiquide, "Air Liquide", model_AirLiquide, "EC.D.AI.CASH.IP"),
    (Renault, "Renault", model_Renault, "EC.D.RENA.CASH.IP"),
    (Carrefour, "Carrefour", model_Carrefour, "EC.D.CA.CASH.IP"),
    (Dassault, "Dassault", model_Dassault, "EC.D.DSY.CASH.IP"),
    (Capgemini, "Capgemini", model_Capgemini, "EC.D.CAPFP.CASH.IP"),
    (Bouygues, "Bouygues", model_bouygues, "EC.D.EN.CASH.IP"),
    (BNPParibas, "BNP Paribas", model_bnp, 'EC.D.BNPP.CASH.IP'),
    (SociétéGénérale, "Société Générale", model_sg, "EC.D.GLEFP.CASH.IP"),
    (Airbus, "Airbus", model_airbus, "EC.D.EAD.CASH.IP"),
    (Unibail, "Unibail", model_Unibail, "EG.D.ULNA.CASH.IP"),
    (Vivendi, "Vivendi", model_Vivendi, "EC.D.VIVFP.CASH.IP"),
    (Total, "Total", model_Total, "EC.D.FP.CASH.IP"),
    (Worldline, "Worldline", model_Worldline, "EC.D.WLNFP.CASH.IP"),
    (Teleperformance, "Teleperformance", model_Teleperformance, "EC.D.RCFFP.CASH.IP"),
    (Stellantis, "Stellantis", model_Stellantis, "EC.D.STLAFP.CASH.IP"),
    (Sodexo, "Sodexo", model_Sodexo, "EC.D.EXHO.CASH.IP"),
    (SchneiderElectric, "Schneider Electric", model_SchneiderElectric, "EC.D.SU.CASH.IP"),
    (Safran, "Safran", model_Safran, "EC.D.SAFFP.CASH.IP"),
    (Publicis, "Publicis", model_Publicis, "EC.D.PUB.CASH.IP"),
    (PernodRicard, "Pernod Ricard", model_PernodRicard, "EC.D.RI.CASH.IP"),
    (Orange, "Orange", model_Orange, "EC.D.FTEFP.CASH.IP"),
    (Michelin, "Michelin", model_Michelin, "EC.D.ML.CASH.IP"),
    (Lvmh, "LVMH", model_LVMH, "EC.D.MCA.CASH.IP"),
    (Loreal, "L'Oréal", model_Loreal, "EC.D.OR.CASH.IP"),
    (Legrand, "Legrand", model_Legrand, "EC.D.LRFP.CASH.IP"),
    (Kering, "Kering", model_Kering, "EC.D.PP.CASH.IP"),
    (Hermes, "Hermes", model_Hermes, "EC.D.RMSFP.CASH.IP"),
    (Essilor, "Essilor", model_Essilor, "EC.D.EF.CASH.IP"),
    (Danone, "Danone", model_Danone, "EC.D.DANO.CASH.IP"),
    (CréditAgricole, "Crédit Agricole", model_CréditAgricole, "EC.D.ACA.CASH.IP"),
    (AXA, "AXA", model_AXA, "EC.D.CS.CASH.IP"),
    (Arcelor, "Arcelor", model_Arcelor, "EG.D.MTNA.CASH.IP"),
    (Alstom, "Alstom", model_Alstom, "EC.D.ALS.CASH.IP"),
    (Engie, "Engie", model_Engie, "EC.D.GSZFP.CASH.IP"),
    (Eurofins, "Eurofins", model_Eurofins, "EC.D.ERFFP.CASH.IP"),
    (Vinci, "Vinci", model_Vinci, "EC.D.DGFP.CASH.IP"),
    (VeoliaEnvironnement, "Veolia", model_VeoliaEnvironnement, "EC.D.VIE.CASH.IP"),
    (Thales, "Thales", model_Thales, "EC.D.HOFP.CASH.IP"),
    (Stmicroelectronics, "Stmicroelectronics", model_Stmicroelectronics, "EC.D.STM.CASH.IP"),
    (Sanofi, "Sanofi", model_Sanofi, "EC.D.SASY.CASH.IP"),
    (SaintGobain, "Saint-Gobain", model_SaintGobain, "EC.D.SGO.CASH.IP")

]

for elemento in lscac:
    today = []
    element = elemento[0].copy()
    element['csqt_up'] = ind.csqt_up(element)

    element['csqt_down'] = ind.csqt_down(element)
    element['csq_var'] = ind.csqt_var(element)

    element["Daily Stock Return"] = ind.dret(element)

    # cac40 = cac40.drop(cac40.index[0:len(cac40)-len(jpmorgan_df)])

    element['Var 5j'] = ind.var5j(element)
    element['SMA 100'] = ind.sma(element, 100)
    element['SMA 20'] = ind.sma(element, 20)
    element['SMA 10'] = ind.sma(element, 10)

    element['SMA Change 100'] = ind.sma_change(element, 100)
    element['SMA Change 20'] = ind.sma_change(element, 20)
    element['SMA Change 10'] = ind.sma_change(element, 10)

    element['CAC40 SMA Change 100'] = ind.sma_change(element, 100)
    element["Volume %"] = ind.dvol(element)

    # element["RSI 14"] = ind.RSI(element, 14)
    element["RSI_TA 14"] = round(ta.momentum.RSIIndicator(element["Adj Close"], 14).rsi(), 2)

    # element["RSI 5"] = ind.RSI(element, 5)
    element["RSI_TA 5"] = round(ta.momentum.RSIIndicator(element["Adj Close"], 5).rsi(), 2)

    # element["RSI 9"] = ind.RSI(element, 9)
    element["RSI_TA 9"] = round(ta.momentum.RSIIndicator(element["Adj Close"], 9).rsi(), 2)

    # element["RSI 25"] = ind.RSI(element, 25)
    element["RSI_TA 25"] = round(ta.momentum.RSIIndicator(element["Adj Close"], 25).rsi(), 2)

    # element["RSI 34"] = ind.RSI(element, 34)
    element["RSI_TA 34"] = round(ta.momentum.RSIIndicator(element["Adj Close"], 34).rsi(), 2)

    element["OBV_TA"] = ta.volume.OnBalanceVolumeIndicator(element["Adj Close"], element["Volume"]).on_balance_volume()
    element["OBV_TA %"] = ind.dobv(element)

    element["TSI_TA"] = ta.momentum.TSIIndicator(element["Adj Close"], 25, 13).tsi()

    element["indice_dow"] = ind.dret(dow)
    element["indice_snp"] = ind.dret(snp)
    element["indice_nasdaq"] = ind.dret(nasdaq)
    element["indice_nikkei"] = ind.dret(nikkei)
    element["indice_ftse"] = ind.dret(ftse)
    element["indice_dax"] = ind.dret(dax)

    element['Var 5j cac40'] = ind.var5j(cac40)
    element['Var 5j dow'] = ind.var5j(dow)
    element['Var 5j snp'] = ind.var5j(snp)
    element['Var 5j nasdaq'] = ind.var5j(nasdaq)
    element['Var 5j ftse'] = ind.var5j(ftse)
    element['Var 5j nikkei'] = ind.var5j(nikkei)
    element['Var 5j dax'] = ind.var5j(dax)

    element["EUR/USD"] = ind.dret(eur_usd)
    element["Gold future"] = ind.dret(gold)
    element["Petrole"] = ind.dret(petrole)

    element['Sharpe Ratio'] = ind.sharpe_ratio(element, 1, 63)
    element['Volatillity'] = ind.volatillity(element, 63)
    element['Cac40 Volatillity'] = ind.volatillity(cac40, 63)
    element['Beta'] = ind.beta(cac40, element, 63)
    today.append(element.iloc[-1])
    element['prediction'] = element['Daily Stock Return'].shift(-1)


    def dhret(r):
        daily2 = r[['High']].copy()
        daily2 = (daily2['High'] / (r['Close'].shift(1)) - 1) * 100
        return daily2.shift(-1)


    def dlret(r):
        daily2 = r[['Low']].copy()
        daily2 = (daily2['Low'] / (r['Close'].shift(1)) - 1) * 100
        return daily2.shift(-1)


    element["prediction_High"] = dhret(element)
    element["prediction_Low"] = dlret(element)

    element = element.dropna()
    # cac40 = cac40.dropna()

    today_df = pd.DataFrame(today)
    today_df = today_df.fillna(0)
    # del today_df['prediction']
    today_df.iloc[-1]
    name = elemento[1]

    print(name)
    today_df = ind.tweet_dt_sentiment(today_df, name)
    print("### Done 2/4 ###")
    today_df = ind.tweet_dt_sentiment(today_df, name, True)
    print("### Done 2/4 ###")
    today_df = ind.tweet_dt_tr_sentiment(today_df, name)
    print("### Done 3/4 ###")
    today_df = ind.tweet_dt_tr_sentiment(today_df, name, True)
    print("### Done 4/4 ###")

    er = load(elemento[2][0])
    er_H = load(elemento[2][1])
    er_L = load(elemento[2][2])

    close_pred = er.predict(today_df[['Volume', 'blob',
                                      'vader_compound', 'vader_posneg', 'own_lexicon_fr', 'blob_close',
                                      'vader_compound_close', 'vader_posneg_close', 'own_lexicon_fr_close',
                                      'tr_lexicon', 'tr_lexicon_close', 'own_lexicon_en',
                                      'own_lexicon_en_close', 'Daily Stock Return', 'csqt_up',
                                      'csqt_down', 'csq_var', 'Var 5j', 'SMA 100', 'SMA 20', 'SMA 10',
                                      'SMA Change 100', 'SMA Change 20', 'SMA Change 10',
                                      'CAC40 SMA Change 100', 'RSI_TA 14', 'RSI_TA 5', 'RSI_TA 9',
                                      'RSI_TA 25', 'RSI_TA 34', 'OBV_TA', 'OBV_TA %', 'TSI_TA', 'indice_dow',
                                      'indice_snp', 'indice_nasdaq', 'indice_nikkei', 'indice_ftse',
                                      'indice_dax', 'Var 5j cac40', 'Var 5j dow', 'Var 5j snp',
                                      'Var 5j nasdaq', 'Var 5j ftse', 'Var 5j nikkei', 'Var 5j dax',
                                      'EUR/USD', 'Gold future', 'Petrole', 'Sharpe Ratio', 'Volatillity',
                                      'Cac40 Volatillity', 'Beta']])

    up_pred = er_H.predict(today_df[['Volume', 'blob',
                                     'vader_compound', 'vader_posneg', 'own_lexicon_fr', 'blob_close',
                                     'vader_compound_close', 'vader_posneg_close', 'own_lexicon_fr_close',
                                     'tr_lexicon', 'tr_lexicon_close', 'own_lexicon_en',
                                     'own_lexicon_en_close', 'Daily Stock Return', 'csqt_up',
                                     'csqt_down', 'csq_var', 'Var 5j', 'SMA 100', 'SMA 20', 'SMA 10',
                                     'SMA Change 100', 'SMA Change 20', 'SMA Change 10',
                                     'CAC40 SMA Change 100', 'RSI_TA 14', 'RSI_TA 5', 'RSI_TA 9',
                                     'RSI_TA 25', 'RSI_TA 34', 'OBV_TA', 'OBV_TA %', 'TSI_TA', 'indice_dow',
                                     'indice_snp', 'indice_nasdaq', 'indice_nikkei', 'indice_ftse',
                                     'indice_dax', 'Var 5j cac40', 'Var 5j dow', 'Var 5j snp',
                                     'Var 5j nasdaq', 'Var 5j ftse', 'Var 5j nikkei', 'Var 5j dax',
                                     'EUR/USD', 'Gold future', 'Petrole', 'Sharpe Ratio', 'Volatillity',
                                     'Cac40 Volatillity', 'Beta']])

    down_pred = er_L.predict(today_df[['Volume', 'blob',
                                       'vader_compound', 'vader_posneg', 'own_lexicon_fr', 'blob_close',
                                       'vader_compound_close', 'vader_posneg_close', 'own_lexicon_fr_close',
                                       'tr_lexicon', 'tr_lexicon_close', 'own_lexicon_en',
                                       'own_lexicon_en_close', 'Daily Stock Return', 'csqt_up',
                                       'csqt_down', 'csq_var', 'Var 5j', 'SMA 100', 'SMA 20', 'SMA 10',
                                       'SMA Change 100', 'SMA Change 20', 'SMA Change 10',
                                       'CAC40 SMA Change 100', 'RSI_TA 14', 'RSI_TA 5', 'RSI_TA 9',
                                       'RSI_TA 25', 'RSI_TA 34', 'OBV_TA', 'OBV_TA %', 'TSI_TA', 'indice_dow',
                                       'indice_snp', 'indice_nasdaq', 'indice_nikkei', 'indice_ftse',
                                       'indice_dax', 'Var 5j cac40', 'Var 5j dow', 'Var 5j snp',
                                       'Var 5j nasdaq', 'Var 5j ftse', 'Var 5j nikkei', 'Var 5j dax',
                                       'EUR/USD', 'Gold future', 'Petrole', 'Sharpe Ratio', 'Volatillity',
                                       'Cac40 Volatillity', 'Beta']])

    print(today_df.index)
    print("Up: ", up_pred, "Close: ", close_pred, "Down: ", down_pred)
    print("Pivot: Up: ", (up_pred / 100 + 1) * today_df["Adj Close"][0], "Close: ",
          (close_pred / 100 + 1) * today_df["Adj Close"][0], "Down: ", (down_pred / 100 + 1) * today_df["Adj Close"][0])
    print("Stop loss UP: ", (up_pred / 100 + 1) * today_df["Adj Close"][0] * (1 + 0.012))
    print("Stop loss DOWN: ", (down_pred / 100 + 1) * today_df["Adj Close"][0] * (1 - 0.012))

    print("############# ", round(i / 40 * 100), "% #############")
    i += 1

    #     try:

    # if (close_pred[0] < 0)&(cdown/(cup+cdown) <= 0.5):
    print(close_pred, "DOWN")
    ig_service.create_working_order(currency_code='EUR', direction='SELL', epic=elemento[3],
    expiry="-", force_open=False, guaranteed_stop='false',
    level=str(round((up_pred/100+1)*today_df["Close"],3)[0]),  time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level=str(round((close_pred/100+1)*today_df["Close"],3)[0]),
    order_type='LIMIT', size=str(int(round(10000/((up_pred/100+1)*today_df["Adj Close"])))),  stop_distance=None, good_till_date=None,deal_reference=None,
    stop_level= str(round((up_pred/100+1)*today_df["Close"]*(1+0.012),3)[0]))

    print(close_pred, "DOWN")
    ig_service.create_working_order(currency_code='EUR', direction='SELL', epic=elemento[3],
    expiry="-", force_open=False, guaranteed_stop='false',
    level=str(round((close_pred/100+1)*today_df["Close"],3)[0]),  time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level=str(round((down_pred/100+1)*today_df["Close"],3)[0]),
    order_type='LIMIT', size=str(int(round(10000/((up_pred/100+1)*today_df["Adj Close"])))),  stop_distance=None, good_till_date=None,deal_reference=None,
    stop_level= str(round((up_pred/100+1)*today_df["Close"]*(1+0.06),3)[0]))

    #             cdown += 1

    #         if (close_pred[0] > 0)&(cup/(cup+cdown) <= 0.5):
    #             print(close_pred, "UP")
    #             ig_service.create_working_order(currency_code='EUR', direction='BUY', epic=elemento[3],
    #             expiry="-", force_open=False, guaranteed_stop='false',
    #             level=str(round((down_pred/100+1)*today_df["Close"],3)[0]),  time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level=str(round((close_pred/100+1)*today_df["Close"],3)[0]),
    #             order_type='LIMIT', size=str(int(round(10000/((up_pred/100+1)*today_df["Adj Close"])))),  stop_distance=None, good_till_date=None,deal_reference=None,
    #             stop_level= str(round((down_pred/100+1)*today_df["Close"]*(1-0.012),3)[0]))

    #             print(close_pred, "UP")
    #             ig_service.create_working_order(currency_code='EUR', direction='BUY', epic=elemento[3],
    #             expiry="-", force_open=False, guaranteed_stop='false',
    #             level= str(round((close_pred/100+1)*today_df["Close"],3)[0]),  time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level=str(round((up_pred/100+1)*today_df["Close"],3)[0]),
    #             order_type='LIMIT', size=str(int(round(10000/((up_pred/100+1)*today_df["Adj Close"])))),  stop_distance=None, good_till_date=None,deal_reference=None,
    #             stop_level= str(round((down_pred/100+1)*today_df["Close"]*(1-0.06),3)[0]))

    #             cup += 1
    #     except:
    #         print("error")

    df_ind.append((name, close_pred[0], up_pred[0], down_pred[0]))

df_cac = pd.DataFrame(df_ind, columns = ["entité", "close_pred", "up_pred", "down_pred"])
df_cac["entité"]

df_cac["entité"].iloc[22] = "Lvmh"
df_cac["entité"].iloc[23] = "L'oreal"
df_cac["entité"].iloc[11] = "TotalEnergies"
df_cac["entité"].iloc[27] = "EssilorLuxottica"
df_cac["entité"].iloc[6] = "Bnp Paribas"
df_cac["entité"].iloc[30] = "Axa"
df_cac["entité"].iloc[3] = "Dassault Systemes"
df_cac["entité"].iloc[29] = "Credit Agricole"
df_cac["entité"].iloc[4] = "CapGemini"
df_cac["entité"].iloc[40] = "Saint Gobain"
df_cac["entité"].iloc[31] = "Arcelor Mittal"
df_cac["entité"].iloc[24] = "Legrand SA"
df_cac["entité"].iloc[7] = "Societe Generale"
df_cac["entité"].iloc[36] = "Veolia Environ."
df_cac["entité"].iloc[34] = "Eurofins Scient."
df_cac["entité"].iloc[18] = "Publicis Groupe"
df_cac["entité"].iloc[9] = "Unibail Rodamco Wes"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table_MN = pd.read_html('https://www.abcbourse.com/marches/ponderation_cac40', match='Poids dans le CAC 40')
poids = table_MN[0].set_index("Société")

df_pred_cac = df_cac.set_index("entité").join(poids).drop("Sodexo")

for i in range(0, len(df_pred_cac)):
    df_pred_cac["Poids dans le CAC 40"].iloc[i] = float(
        df_pred_cac["Poids dans le CAC 40"].iloc[i][:-1].replace(",", ".")) / 100

p1 = sum(df_pred_cac["Poids dans le CAC 40"]*df_pred_cac["close_pred"])
p2 = sum(df_pred_cac["Poids dans le CAC 40"]*df_pred_cac["up_pred"])
p3 = sum(df_pred_cac["Poids dans le CAC 40"]*df_pred_cac["down_pred"])

print((p3/100+1)*cac40.iloc[-1]["Close"])
print(p1)
print((p2/100+1)*cac40.iloc[-1]["Close"])
print(p2)
print((p1/100+1)*cac40.iloc[-1]["Close"])
print(p3)

# if p1 < 0:
print(p1, "DOWN")
ig_service.create_working_order(currency_code='EUR', direction='SELL', epic="IX.D.CAC.IFM.IP",
expiry="-", force_open=False, guaranteed_stop='false',
level=str(round((p2/100+1)*cac40.iloc[-1]["Close"],3)),  time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level=str(round((p1/100+1)*cac40.iloc[-1]["Close"],3)),
order_type='LIMIT', size=str(int(round(10000/((p2/100+1)*cac40.iloc[-1]["Close"])))),  stop_distance=None, good_till_date=None,deal_reference=None,
stop_level= str(round((p2/100+1)*cac40.iloc[-1]["Close"]*(1+0.012),3)))

if p1 < 0:
    print(p1, "DOWN")
    ig_service.create_working_order(currency_code='EUR', direction='SELL', epic="IX.D.CAC.IFM.IP",
    expiry="-", force_open=False, guaranteed_stop='false',
    level=str(round((p1/100+1)*cac40.iloc[-1]["Close"],3)),  time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level=str(round((p3/100+1)*cac40.iloc[-1]["Close"],3)),
    order_type='LIMIT', size=str(int(round(10000/((p2/100+1)*cac40.iloc[-1]["Close"])))),  stop_distance=None, good_till_date=None,deal_reference=None,
    stop_level= str(round((p2/100+1)*cac40.iloc[-1]["Close"],3)))

if p1 > 0:

    print(p1, "UP")
    ig_service.create_working_order(currency_code='EUR', direction='BUY', epic="IX.D.CAC.IFM.IP",
    expiry="-", force_open=False, guaranteed_stop='false',
    level=str(round((p1/100+1)*cac40.iloc[-1]["Close"],3)),  time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level=str(round((p2/100+1)*cac40.iloc[-1]["Close"],3)),
    order_type='LIMIT', size=str(int(round(10000/((p2/100+1)*cac40.iloc[-1]["Close"])))),  stop_distance=None, good_till_date=None,deal_reference=None,
    stop_level= str(round((p3/100+1)*cac40.iloc[-1]["Close"],3)))


# print(p1, "UP")
ig_service.create_working_order(currency_code='EUR', direction='BUY', epic="IX.D.CAC.IFM.IP",
expiry="-", force_open=False, guaranteed_stop='false',
level=str(round((p3/100+1)*cac40.iloc[-1]["Close"],3)),  time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level=str(round((p1/100+1)*cac40.iloc[-1]["Close"],3)),
order_type='LIMIT', size=str(int(round(10000/((p2/100+1)*cac40.iloc[-1]["Close"])))),  stop_distance=None, good_till_date=None,deal_reference=None,
stop_level= str(round((p3/100+1)*cac40.iloc[-1]["Close"]*(1-0.012),3)))