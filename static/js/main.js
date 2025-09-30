document.addEventListener('DOMContentLoaded', () => {
    lucide.createIcons();

    const tabText = document.getElementById('tab-text');
    const tabFile = document.getElementById('tab-file');
    const textInputArea = document.getElementById('text-input-area');
    const fileInputArea = document.getElementById('file-input-area');
    const emailForm = document.getElementById('email-form');
    const emailFile = document.getElementById('email-file');
    const fileNameDisplay = document.getElementById('file-name');
    const removeFileBtn = document.getElementById('remove-file-btn');

    const inputSection = document.getElementById('input-section');
    const loadingSection = document.getElementById('loading-section');
    const mainCard = document.getElementById('main-card');

    const suggestedReply = document.getElementById('suggested-reply');

    const copyButton = document.getElementById('copy-button');
    const copyFeedback = document.getElementById('copy-feedback');
    const resetButton = document.getElementById('reset-button');

    tabText.addEventListener('click', () => {
        tabText.classList.add('text-indigo-600', 'border-indigo-600');
        tabText.classList.remove('text-slate-500');
        tabFile.classList.add('text-slate-500');
        tabFile.classList.remove('text-indigo-600', 'border-indigo-600');
        textInputArea.classList.remove('hidden');
        fileInputArea.classList.add('hidden');
    });

    tabFile.addEventListener('click', () => {
        tabFile.classList.add('text-indigo-600', 'border-indigo-600');
        tabFile.classList.remove('text-slate-500');
        tabText.classList.add('text-slate-500');
        tabText.classList.remove('text-indigo-600', 'border-indigo-600');
        fileInputArea.classList.remove('hidden');
        textInputArea.classList.add('hidden');
    });

    emailFile.addEventListener('change', () => {
        if (emailFile.files.length > 0) {
            const file = emailFile.files[0];
            const validTypes = ['application/pdf', 'text/plain'];
            const fileName = file.name.toLowerCase();
            const isValidExtension = fileName.endsWith('.pdf') || fileName.endsWith('.txt');
            const isValidType = validTypes.includes(file.type);

            if (!isValidExtension && !isValidType) {
                alert('Por favor, selecione apenas arquivos PDF ou TXT.');
                emailFile.value = '';
                fileNameDisplay.textContent = '';
                removeFileBtn.classList.add('hidden');
                return;
            }

            fileNameDisplay.textContent = file.name;
            removeFileBtn.classList.remove('hidden');
        } else {
            fileNameDisplay.textContent = '';
            removeFileBtn.classList.add('hidden');
        }
    });

    removeFileBtn.addEventListener('click', () => {
        emailFile.value = '';
        fileNameDisplay.textContent = '';
        emailFile.disabled = false;
        removeFileBtn.classList.add('hidden');
    });

    emailForm.addEventListener('submit', () => {
        inputSection.classList.add('hidden');
        loadingSection.classList.remove('hidden');
        mainCard.classList.add('py-12');
    });

    if (copyButton && suggestedReply && copyFeedback) {
        copyButton.addEventListener('click', () => {
            navigator.clipboard.writeText(suggestedReply.textContent.trim());
            copyFeedback.style.opacity = 1;
            setTimeout(() => {
                copyFeedback.style.opacity = 0;
            }, 1200);
        });
    }

    if (resetButton) {
        resetButton.addEventListener('click', () => {
            window.location.href = '/';
        });
    }
});