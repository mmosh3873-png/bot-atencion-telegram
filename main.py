python
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
 keyboard = [
 [InlineKeyboardButton("¿Cómo empezar?", callback_data="start_info")],
 [InlineKeyboardButton("Opciones con poco capital", callback_data="options")],
 [InlineKeyboardButton("Información importante", callback_data="important")],
 [InlineKeyboardButton("Preguntas frecuentes", callback_data="faq")],
 [InlineKeyboardButton(" Hablar con un asesor", url="https://t.me/Dobled2357")]
 ]

 reply_markup = InlineKeyboardMarkup(keyboard)

 await update.message.reply_text(
 " Bienvenido/a\n\n"
 "Aquí encontrarás información clara para comenzar a generar ingresos invirtiendo montos accesibles, "
 "con un enfoque práctico y responsable.\n\n"
 "Selecciona una opción del menú para continuar ⬇",
 reply_markup=reply_markup
 )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
 query = update.callback_query
 await query.answer()

 responses = {
 "start_info": (
 "El primer paso es entender cómo funcionan las inversiones y definir un objetivo claro.\n\n"
 " Empieza con montos medianos para que tus ganancias a corto plazo fructifiquen\n"
 " Usa capital destinado a inversión\n"
 " Con nosotros no hay riesgo\n"
 " tendras ganancias a corto plazo"
 ),
 "options": (
 "Existen alternativas para iniciar con montos accesibles:\n\n"
 "• Modelos de inversión de bajo monto\n"
 "• En mi Plataforma digitale con entrada reducida no pierdes ya que mi metodo es 100% confiable\n"
 "• Porque mi Educación financiera aplicada me respalda\n"
 "• Manejo mis Estrategias progresivas\n\n"
 "Cada opción tiene distintos niveles de riesgo pero con mis conocimeintos no hay perdida."
 ),
 "important": (
 "Antes de invertir considera que en poco tiempo podras disfrutar de tus ingresos generados con tu inversion:\n\n"
 "• existen ganancias garantizadas\n"
 "• Toda inversión implica riesgo pero no para alguien con conocimientos en la materia de inversion\n"
 "• Los resultados dependen de múltiples factores\n"
 "• Es clave tomar decisiones informadas con nosotros no estas sol@"
 ),
 "faq": (
 " ¿Se necesita experiencia previa?\n"
 "No. porque yo hare todo el proceso de inversion por ti\n\n"
 " ¿Cuánto dinero se requiere?\n"
 "Depende de la opción elegida. Hay alternativas con montos bajos.\n\n"
 " ¿Es seguro invertir?\n"
 "Con nosotros como instrumento y de cómo se gestione el riesgo es muy seguro."
 )
 }

 await query.edit_message_text(responses[query.data])

def main():
 app = ApplicationBuilder().token(TOKEN).build()
 app.add_handler(CommandHandler("start", start))
 app.add_handler(CallbackQueryHandler(buttons))
 app.run_polling()

if name
