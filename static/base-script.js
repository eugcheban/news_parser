document.getElementById('toggle-sidebar').addEventListener('click', function() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('hidden');
});

$('#header-title').click(function() {
    window.location.href = 'https://example.com';
});