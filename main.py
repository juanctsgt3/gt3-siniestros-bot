import asyncio
import logging
import datetime
import pandas as pd
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.constants import ParseMode

# ============ CONFIGURACIÓN ============
TELEGRAM_TOKEN = '8117221184:AAEHOLFXRy567KRtHltbCTEx0rfb7fn7UKA'
USER_ID = 704277362

WEBS = {
    'PLC Auction': 'https://plc.auction/es/auction/from-de/porsche/911',
    'Copart': 'https://www.copart.com/lotSearchResults',
    'A Better Bid': 'https://abetter.bid/en/car-finder/model-911/year-2013-2025?search_query=Porsche+911+',
    'Mobile.de': 'https://m.mobile.de/auto/search.html?cn=DE&dam=true&ms=20100%3B28%3B%3B&od=up&ref=dsp&s=Car&sb=rel&vc=Car',
    'Dubizzle': 'https://www.dubizzle.com/motors/used-cars/porsche/911/',
    'CarsFromWest': 'https://carsfromwest.com/',
    'AutoDNA': 'https://www.autodna.com/',
    'Copart UK': 'https://www.copart.co.uk/lotSearchResults',
    'SalvageMarket UK': 'https://www.salvagemarket.co.uk/Search?searchText=porsche%20911',
    'Standvirtual PT': 'https://www.standvirtual.com/carros/porsche/911/',
    'Leboncoin FR': 'https://www.leboncoin.fr/recherche?text=porsche%20911%20gt3%20accident%C3%A9',
    'Autoscout24 IT': 'https://www.autoscout24.it/',
    'Rennlist': 'https://rennlist.com/forums/marketplace/',
    'Facebook Marketplace': 'https://www.facebook.com/marketplace/',
    'AutoScout24 EU': 'https://www.autoscout24.es/lst/porsche/992/ve_gt3?atype=C&cy=D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL&desc=0&powertype=kw&search_id=1qnsjfh2yjo&sort=standard&ustate=A',
    'IAAI Global': 'https://www.iaai.com/Search?url=fWKBIzm5vlJ9CQqZKqq7rtcwGIzX5ILavqfA30taAYA%3d',
    'IAAI GT3 Touring': 'https://www.iaai.com/VehicleDetail/42512601~US',
    'Auto.ria.com': 'https://auto.ria.com/car/porsche/911/',
    'Otomoto.pl': 'https://www.otomoto.pl/osobowe/porsche/911/',
    'Autovit.ro': 'https://www.autovit.ro/autoturisme/porsche/911/'
}

# ============ FUNCIONES ============
async def resumen_diario() -> str:
    fecha = datetime.datetime.now().strftime("%d/%m/%Y")
    mensaje = f"✈️ <b>Resultados diarios GT3 siniestrados ({fecha})</b>\n"
    for nombre, url in WEBS.items():
        mensaje += f"• <b>{nombre}</b>: <a href='{url}'>ver resultados</a>\n"
    mensaje += "\n✅ Bot operativo 24/7. Te avisaré si aparece algo interesante."
    return mensaje

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Bot operativo. Puedes usar /prueba para ver el resumen diario.")

async def prueba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = await resumen_diario()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje, parse_mode=ParseMode.HTML)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prueba", prueba))
    app.run_polling()

if __name__ == '__main__':
    main()
