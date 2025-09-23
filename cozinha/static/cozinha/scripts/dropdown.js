
const dropdown = document.getElementById('dropdown-container');
const dropdownToggleBtn = document.getElementById('dropdown-toggle-btn');
const dropdownCloseBtn = document.getElementById('dropdown-close-btn');

const modalBackdrop = document.getElementById('modal-backdrop');

const menuExecutivoModal = document.getElementById('menu-executivo');
const menuExecutivoBtn = document.getElementById('menu-executivo-btn');
const menuExecutivoCloseBtn = document.getElementById('menu-executivo-close-btn');

const contratarAgoraBtn = document.getElementById('contratar-agora-btn');

const sobreNosModal = document.getElementById('sobre-nos');
const sobreNosBtn = document.getElementById('sobre-nos-btn');
const sobreNosCloseBtn = document.getElementById('sobre-nos-close-btn');

const servicosModal = document.getElementById('servicos');
const servicosBtn = document.getElementById('servicos-btn');
const servicosCloseBtn = document.getElementById('servicos-close-btn');

function toggleElement(element) {
    element.classList.toggle('on');
}

dropdownToggleBtn.addEventListener('click', () => {
    toggleElement(dropdown);
    toggleElement(modalBackdrop);
});

dropdownCloseBtn.addEventListener('click', () => {
    toggleElement(dropdown);
    toggleElement(modalBackdrop);
});

menuExecutivoBtn.addEventListener('click', () => {
    toggleElement(menuExecutivoModal);
})

menuExecutivoCloseBtn.addEventListener('click', () => {
    toggleElement(menuExecutivoModal);
})

servicosBtn.addEventListener('click', () => {
    toggleElement(servicosModal);
})

servicosCloseBtn.addEventListener('click', () => {
    toggleElement(servicosModal);
})

sobreNosBtn.addEventListener('click', () => {
    toggleElement(sobreNosModal);
})

sobreNosCloseBtn.addEventListener('click', () => {
    toggleElement(sobreNosModal);
})