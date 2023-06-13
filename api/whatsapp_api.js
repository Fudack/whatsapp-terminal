const qrcode = require('qrcode-terminal');
const fs = require('fs');
const path = require('path');
const { Client } = require('whatsapp-web.js');
const { exec } = require('child_process');

const client = new Client();

client.on('qr', qr => {
  qrcode.generate(qr, { small: true });
});

// Evento de conexión exitosa
client.on('ready', () => {
  console.log('Cliente de WhatsApp listo y conectado');
});

// Evento de recepción de mensajes
client.on('message', async (message) => {
  const remitente = await getContactName(message.from);
  const contenido = message.body;

  // Escribir en un archivo de texto
  const texto = `Remitente: ${remitente}\nMensaje: ${contenido}\n\n`;
  const fileName = `chat${message.from}.txt`;  
  const filePath = path.join(__dirname, '..', 'db', fileName);
  fs.appendFile(filePath, texto, (err) => {
    if (err) {
      console.error('Error al escribir en el archivo:', err);
    } else {
      // Ejecutar el script de Python para leer el último mensaje
      const pythonScriptPath = path.join(__dirname, '..', 'main', 'tts.py');
      const pythonCommand = `python3 ${pythonScriptPath} ${filePath}`;
      exec(pythonCommand, (error, stdout, stderr) => {
        if (error) {
          console.error('Error al ejecutar el script de Python:', error);
          return;
        }
  
        console.log('Último mensaje leído:');
        console.log(stdout);
      });
    }
  });
});

// Función para obtener el nombre del contacto a partir del número de teléfono
async function getContactName(contactId) {
  const contact = await client.getContactById(contactId);
  if (contact && contact.name) {
    return contact.name;
  }
  return contactId;
}

// Inicializar el cliente de WhatsApp
client.initialize();
