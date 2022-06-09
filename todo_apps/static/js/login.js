const loader = document.getElementById('loader')
const loading = document.getElementById('loading')
const form = document.getElementById('auth-form')

function redirect() {
    form.style.display = "none";
    loader.style.display = "block";
    loading.style.display = "block";
    setTimeout(() => {
        window.location.href = "/";
    }, 1300);
};

document.body.addEventListener('htmx:configRequest', (e) => {
    e.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
})