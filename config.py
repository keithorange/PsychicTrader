# Directory to store session history data
HISTORY_DIR = './history'

# Crypto pairs used
ALL_CRYPTO_PAIRS = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'NEO/USDT', 'LTC/USDT', 'QTUM/USDT', 'ADA/USDT', 'XRP/USDT', 'EOS/USDT', 'TUSD/USDT', 'IOTA/USDT', 'XLM/USDT', 'ONT/USDT', 'TRX/USDT', 'ETC/USDT', 'ICX/USDT', 'NULS/USDT', 'VET/USDT', 'USDC/USDT', 'LINK/USDT', 'WAVES/USDT', 'ONG/USDT', 'HOT/USDT', 'ZIL/USDT', 'ZRX/USDT', 'FET/USDT', 'BAT/USDT', 'XMR/USDT', 'ZEC/USDT', 'IOST/USDT', 'CELR/USDT', 'DASH/USDT', 'OMG/USDT', 'THETA/USDT', 'ENJ/USDT', 'MATIC/USDT', 'ATOM/USDT', 'TFUEL/USDT', 'ONE/USDT', 'FTM/USDT', 'ALGO/USDT', 'DOGE/USDT', 'DUSK/USDT', 'ANKR/USDT', 'WIN/USDT', 'COS/USDT', 'MTL/USDT', 'TOMO/USDT', 'PERL/USDT', 'DENT/USDT', 'KEY/USDT', 'DOCK/USDT', 'WAN/USDT', 'FUN/USDT', 'CVC/USDT', 'CHZ/USDT', 'BAND/USDT', 'BUSD/USDT', 'XTZ/USDT', 'REN/USDT', 'RVN/USDT', 'HBAR/USDT', 'NKN/USDT', 'STX/USDT', 'KAVA/USDT', 'ARPA/USDT', 'IOTX/USDT', 'RLC/USDT', 'CTXC/USDT', 'BCH/USDT', 'TROY/USDT', 'VITE/USDT', 'EUR/USDT', 'OGN/USDT', 'DREP/USDT', 'WRX/USDT', 'BTS/USDT', 'LSK/USDT', 'BNT/USDT', 'LTO/USDT', 'MBL/USDT', 'COTI/USDT', 'STPT/USDT', 'WTC/USDT', 'DATA/USDT', 'SOL/USDT', 'CTSI/USDT', 'HIVE/USDT', 'CHR/USDT', 'BTCUP/USDT', 'BTCDOWN/USDT', 'ARDR/USDT', 'MDT/USDT', 'STMX/USDT', 'KNC/USDT', 'LRC/USDT', 'PNT/USDT', 'COMP/USDT', 'SC/USDT', 'ZEN/USDT', 'SNX/USDT', 'ETHUP/USDT', 'ETHDOWN/USDT', 'VTHO/USDT', 'DGB/USDT', 'GBP/USDT', 'SXP/USDT', 'MKR/USDT', 'DCR/USDT', 'STORJ/USDT', 'BNBUP/USDT', 'BNBDOWN/USDT', 'MANA/USDT', 'YFI/USDT', 'BAL/USDT', 'BLZ/USDT', 'IRIS/USDT', 'KMD/USDT', 'JST/USDT', 'ANT/USDT', 'CRV/USDT', 'SAND/USDT', 'OCEAN/USDT', 'NMR/USDT', 'DOT/USDT', 'LUNA/USDT', 'RSR/USDT', 'PAXG/USDT', 'WNXM/USDT', 'TRB/USDT', 'SUSHI/USDT', 'KSM/USDT', 'EGLD/USDT', 'DIA/USDT', 'RUNE/USDT', 'FIO/USDT', 'UMA/USDT', 'BEL/USDT', 'WING/USDT', 'UNI/USDT', 'OXT/USDT', 'SUN/USDT', 'AVAX/USDT', 'FLM/USDT', 'ORN/USDT', 'UTK/USDT', 'XVS/USDT', 'ALPHA/USDT', 'AAVE/USDT', 'NEAR/USDT', 'FIL/USDT', 'INJ/USDT', 'AUDIO/USDT', 'CTK/USDT', 'AKRO/USDT', 'AXS/USDT', 'HARD/USDT', 'STRAX/USDT', 'UNFI/USDT', 'ROSE/USDT', 'AVA/USDT', 'XEM/USDT', 'SKL/USDT', 'GRT/USDT', 'JUV/USDT', 'PSG/USDT', '1INCH/USDT', 'REEF/USDT', 'OG/USDT', 'ATM/USDT', 'ASR/USDT', 'CELO/USDT', 'RIF/USDT', 'TRU/USDT', 'CKB/USDT', 'TWT/USDT', 'FIRO/USDT', 'LIT/USDT', 'SFP/USDT', 'DODO/USDT',
                    'CAKE/USDT', 'ACM/USDT', 'BADGER/USDT', 'FIS/USDT', 'OM/USDT', 'POND/USDT', 'DEGO/USDT', 'ALICE/USDT', 'LINA/USDT', 'PERP/USDT', 'SUPER/USDT', 'CFX/USDT', 'TKO/USDT', 'PUNDIX/USDT', 'TLM/USDT', 'BAR/USDT', 'FORTH/USDT', 'BAKE/USDT', 'BURGER/USDT', 'SLP/USDT', 'SHIB/USDT', 'ICP/USDT', 'AR/USDT', 'POLS/USDT', 'MDX/USDT', 'MASK/USDT', 'LPT/USDT', 'XVG/USDT', 'ATA/USDT', 'GTC/USDT', 'ERN/USDT', 'KLAY/USDT', 'PHA/USDT', 'BOND/USDT', 'MLN/USDT', 'DEXE/USDT', 'C98/USDT', 'CLV/USDT', 'QNT/USDT', 'FLOW/USDT', 'TVK/USDT', 'MINA/USDT', 'RAY/USDT', 'FARM/USDT', 'ALPACA/USDT', 'QUICK/USDT', 'MBOX/USDT', 'FOR/USDT', 'REQ/USDT', 'GHST/USDT', 'WAXP/USDT', 'GNO/USDT', 'XEC/USDT', 'ELF/USDT', 'DYDX/USDT', 'IDEX/USDT', 'VIDT/USDT', 'USDP/USDT', 'GALA/USDT', 'ILV/USDT', 'YGG/USDT', 'SYS/USDT', 'DF/USDT', 'FIDA/USDT', 'FRONT/USDT', 'CVP/USDT', 'AGLD/USDT', 'RAD/USDT', 'BETA/USDT', 'RARE/USDT', 'LAZIO/USDT', 'CHESS/USDT', 'ADX/USDT', 'AUCTION/USDT', 'DAR/USDT', 'BNX/USDT', 'MOVR/USDT', 'CITY/USDT', 'ENS/USDT', 'KP3R/USDT', 'QI/USDT', 'PORTO/USDT', 'POWR/USDT', 'VGX/USDT', 'JASMY/USDT', 'AMP/USDT', 'PLA/USDT', 'PYR/USDT', 'RNDR/USDT', 'ALCX/USDT', 'SANTOS/USDT', 'MC/USDT', 'BICO/USDT', 'FLUX/USDT', 'FXS/USDT', 'VOXEL/USDT', 'HIGH/USDT', 'CVX/USDT', 'PEOPLE/USDT', 'OOKI/USDT', 'SPELL/USDT', 'JOE/USDT', 'ACH/USDT', 'IMX/USDT', 'GLMR/USDT', 'LOKA/USDT', 'SCRT/USDT', 'API3/USDT', 'BTTC/USDT', 'ACA/USDT', 'XNO/USDT', 'WOO/USDT', 'ALPINE/USDT', 'T/USDT', 'ASTR/USDT', 'GMT/USDT', 'KDA/USDT', 'APE/USDT', 'BSW/USDT', 'BIFI/USDT', 'MULTI/USDT', 'STEEM/USDT', 'MOB/USDT', 'NEXO/USDT', 'REI/USDT', 'GAL/USDT', 'LDO/USDT', 'EPX/USDT', 'OP/USDT', 'LEVER/USDT', 'STG/USDT', 'LUNC/USDT', 'GMX/USDT', 'POLYX/USDT', 'APT/USDT', 'OSMO/USDT', 'HFT/USDT', 'PHB/USDT', 'HOOK/USDT', 'MAGIC/USDT', 'HIFI/USDT', 'RPL/USDT', 'PROS/USDT', 'AGIX/USDT', 'GNS/USDT', 'SYN/USDT', 'VIB/USDT', 'SSV/USDT', 'LQTY/USDT', 'AMB/USDT', 'BETH/USDT', 'USTC/USDT', 'GAS/USDT', 'GLM/USDT', 'PROM/USDT', 'QKC/USDT', 'UFT/USDT', 'ID/USDT', 'ARB/USDT', 'LOOM/USDT', 'OAX/USDT', 'RDNT/USDT', 'WBTC/USDT', 'EDU/USDT', 'SUI/USDT', 'AERGO/USDT', 'PEPE/USDT', 'FLOKI/USDT', 'AST/USDT', 'SNT/USDT', 'COMBO/USDT', 'MAV/USDT', 'PENDLE/USDT', 'ARKM/USDT', 'WBETH/USDT', 'WLD/USDT', 'FDUSD/USDT', 'SEI/USDT', 'CYBER/USDT']

# Settings related to the Flask app, database connections, etc. can also be added here