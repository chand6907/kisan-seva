// Current section being edited
let currentSection = '';

// Open the edit modal
function openEditModal(section) {
    currentSection = section;
    const modal = document.getElementById('editModal');
    const modalTitle = document.getElementById('modal-title');
    const formContainer = document.getElementById('edit-form-container');
    
    // Clear previous form
    formContainer.innerHTML = '';
    
    // Set modal title and create form based on section
    switch(section) {
        case 'hero-section':
            modalTitle.textContent = 'Edit Hero Section';
            let heroForm = `
                <div class="form-group">
                    <label for="hero-title-input">Hero Title</label>
                    <input type="text" id="hero-title-input" class="form-control" value="${document.getElementById('hero-title').textContent}">
                </div>
                <div class="form-group">
                    <label for="hero-text-input">Hero Text</label>
                    <textarea id="hero-text-input" class="form-control">${document.getElementById('hero-text').textContent}</textarea>
                </div>
                <div class="form-buttons">
                    <button class="btn" onclick="saveContent('hero-section')">Save Changes</button>
                </div>
            `;
            formContainer.innerHTML = heroForm;
            break;
            
        case 'features-header':
            modalTitle.textContent = 'Edit Features Header';
            let featuresHeaderForm = `
                <div class="form-group">
                    <label for="features-title-input">Features Title</label>
                    <input type="text" id="features-title-input" class="form-control" value="${document.querySelector('.features .section-header h2').textContent}">
                </div>
                <div class="form-group">
                    <label for="features-text-input">Features Description</label>
                    <textarea id="features-text-input" class="form-control">${document.querySelector('.features .section-header p').textContent}</textarea>
                </div>
                <div class="form-buttons">
                    <button class="btn" onclick="saveContent('features-header')">Save Changes</button>
                </div>
            `;
            formContainer.innerHTML = featuresHeaderForm;
            break;
        
        case 'feature1':
        case 'feature2':
        case 'feature3':
        case 'feature4':
        case 'feature5':
            const featureNum = section.charAt(section.length - 1);
            modalTitle.textContent = `Edit Feature ${featureNum}`;
            let featureForm = `
                <div class="form-group">
                    <label for="${section}-title-input">Feature Title</label>
                    <input type="text" id="${section}-title-input" class="form-control" value="${document.getElementById(`${section}-title`).textContent}">
                </div>
                <div class="form-group">
                    <label for="${section}-text-input">Feature Description</label>
                    <textarea id="${section}-text-input" class="form-control">${document.getElementById(`${section}-text`).textContent}</textarea>
                </div>
                <div class="form-buttons">
                    <button class="btn" onclick="saveContent('${section}')">Save Changes</button>
                </div>
            `;
            formContainer.innerHTML = featureForm;
            break;
        
        case 'testimonials-header':
            modalTitle.textContent = 'Edit Testimonials Header';
            let testimonialsHeaderForm = `
                <div class="form-group">
                    <label for="testimonials-title-input">Testimonials Title</label>
                    <input type="text" id="testimonials-title-input" class="form-control" value="${document.querySelector('.testimonials .section-header h2').textContent}">
                </div>
                <div class="form-group">
                    <label for="testimonials-text-input">Testimonials Description</label>
                    <textarea id="testimonials-text-input" class="form-control">${document.querySelector('.testimonials .section-header p').textContent}</textarea>
                </div>
                <div class="form-buttons">
                    <button class="btn" onclick="saveContent('testimonials-header')">Save Changes</button>
                </div>
            `;
            formContainer.innerHTML = testimonialsHeaderForm;
            break;
            
        case 'testimonial1':
        case 'testimonial2':
            const testimonialNum = section.charAt(section.length - 1);
            modalTitle.textContent = `Edit Testimonial ${testimonialNum}`;
            let testimonialForm = `
                <div class="form-group">
                    <label for="${section}-text-input">Testimonial</label>
                    <textarea id="${section}-text-input" class="form-control">${document.getElementById(`${section}-text`).textContent}</textarea>
                </div>
                <div class="form-group">
                    <label for="${section}-name-input">Name</label>
                    <input type="text" id="${section}-name-input" class="form-control" value="${document.getElementById(`${section}-name`).textContent}">
                </div>
                <div class="form-buttons">
                    <button class="btn" onclick="saveContent('${section}')">Save Changes</button>
                </div>
            `;
            formContainer.innerHTML = testimonialForm;
            break;
    }
}

// Save content function
function saveContent(section) {
    const textInput = document.getElementById(`${section}-text-input`);
    const nameInput = document.getElementById(`${section}-name-input`);
    if (textInput) {
        document.getElementById(`${section}-text`).textContent = textInput.value;
    }
    if (nameInput) {
        document.getElementById(`${section}-name`).textContent = nameInput.value;
    }
    alert('Changes saved successfully!');
}

// Dark mode toggle
document.getElementById('darkModeToggle').addEventListener('click', function () {
    document.body.classList.toggle('dark-mode');
});