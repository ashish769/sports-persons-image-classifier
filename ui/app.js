document.getElementById("fileElem").addEventListener("change", function (e) {
    const file = e.target.files[0];
    const preview = document.getElementById("preview");
  
    if (file) {
      const reader = new FileReader();
      reader.onload = function (event) {
        preview.src = event.target.result;
        preview.style.display = "block";
        preview.dataset.base64 = event.target.result;
      };
      reader.readAsDataURL(file);
    }
  });
  
  document.getElementById("upload-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    
    const preview = document.getElementById("preview");
    const errorDiv = document.getElementById("error");
    const resultDiv = document.getElementById("result");
  
    errorDiv.classList.add("hidden");
    resultDiv.classList.add("hidden");
  
    const base64Image = preview.dataset.base64;
  
    if (!base64Image) {
      errorDiv.textContent = "Please select a valid image.";
      errorDiv.classList.remove("hidden");
      return;
    }
  
    const formData = new FormData();
    formData.append("image_data", base64Image);
  
    try {
      const response = await fetch("http://127.0.0.1:5000/classify-image", {
        method: "POST",
        body: formData,
      });
  
      if (!response.ok) throw new Error("Failed to classify image.");
  
      const data = await response.json();
      const prediction = data[0]['class'];
  
      resultDiv.innerHTML = `
        <h3>Prediction: ${prediction}</h3>
        <img src="/static/reference_images/${prediction.toLowerCase().replace(/ /g, "_")}.jpg" alt="${prediction}"/>
      `;
      resultDiv.classList.remove("hidden");
  
    } catch (error) {
      console.error(error);
      errorDiv.textContent = "Error: Could not classify the image.may be the faces cannot detected properly";
      errorDiv.classList.remove("hidden");
    }
  });
  