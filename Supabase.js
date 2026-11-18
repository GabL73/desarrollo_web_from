const SUPABASE_URL = "https://zwmpqtcaftxlppffccla.supabase.co";
const SUPABASE_KEY = "sb_publishable_ErteiUo9UwQV-tEBx9W5aQ_O9ltHbAL";

const supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_KEY);

const form = document.getElementById("formCita");
const mensaje = document.getElementById("mensaje");
const lista = document.getElementById("listaCitas");

async function cargarCitas() {
  const { data, error } = await supabaseClient.from("citas").select("*").order("id", { ascending: false });
  if (error) {
    lista.innerHTML = "<li>Error al cargar: " + error.message + "</li>";
    return;
  }
  lista.innerHTML = "";
  data.forEach(c => {
    const li = document.createElement("li");
    li.textContent = `${c.nombre} - ${c.servicio} - ${c.fecha} ${c.hora}`;
    lista.appendChild(li);
  });
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const datos = {
    nombre: document.getElementById("nombre").value,
    telefono: document.getElementById("telefono").value,
    servicio: document.getElementById("servicio").value,
    fecha: document.getElementById("fecha").value,
    hora: document.getElementById("hora").value,
  };
  const { error } = await supabaseClient.from("citas").insert([datos]);
  if (error) {
    mensaje.textContent = "❌ Error: " + error.message;
  } else {
    mensaje.textContent = "✅ Cita guardada en Supabase!";
    form.reset();
    cargarCitas();
  }
});

cargarCitas();