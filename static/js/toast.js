function showToast(title, message, type = 'normal', duration = 2000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'text-red-600',
        'bg-green-50', 'text-green-600',
        'bg-white', 'text-gray-800'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-green-50', 'text-green-600');
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'text-red-600');
    } else {
        toastComponent.classList.add('bg-white', 'text-gray-800');
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-0');
    toastComponent.classList.add('opacity-90', 'translate-y-16');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-90', 'translate-y-16');
        toastComponent.classList.add('opacity-0', 'translate-y-0');
    }, duration);
}