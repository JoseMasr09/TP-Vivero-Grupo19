function validateForm() {
  var name = document.getElementById("name").value.trim();
  var phone = document.getElementById("phone").value.trim();
  var email = document.getElementById("email").value.trim();
  var message = document.getElementById("message").value.trim();

  var nameError = document.getElementById("nameError");
  var phoneError = document.getElementById("phoneError");
  var emailError = document.getElementById("emailError");
  var messageError = document.getElementById("messageError");


  if (name === "" || phone === "" || email === "" || message === "") {
    alert("Complete los espacios en blanco");
    return false;
  }

  // Verificar que el nombre solo contenga letras
  var namePattern = /^[A-Za-z]+$/;
  if (!namePattern.test(name)) {
    nameError.textContent = "El nombre solo puede contener letras";
    return false;
  }


  // Verificar que el teléfono solo contenga números y tenga exactamente 10 dígitos
  var phonePattern = /^\d{10}$/;
  if (!phonePattern.test(phone)) {
    phoneError.textContent = "El teléfono debe contener exactamente 10 dígitos";
    return false;
  }

  // Verificar el formato del correo electrónico
  var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    emailError.textContent = "Por favor, ingresa un email válido";
    return false;
  }

  // Si todas las validaciones son exitosas, enviar el formulario
  alert("Formulario enviado correctamente.");
  return true;
}