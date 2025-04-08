document.getElementById('input_form').addEventListener('submit', async (event) => {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    // Получаем данные из формы
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;

    console.log('Login:', login); // Отладочное сообщение
    console.log('Password:', password); // Отладочное сообщение

    if (!login || !password) {
        document.getElementById('message').textContent = 'Заполните все поля';
        return;
    }

    try {
        // Отправляем POST-запрос к API
        const response = await fetch('/autorizatoin/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ login, password })
        });

        if (!response.ok) {
            // Если сервер вернул ошибку
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Ошибка авторизации');
        }

        // Получаем данные из ответа
        const data = await response.json();

        // Перенаправляем на страницу аккаунта
        window.location.href = '/account';
    } catch (error) {
        // Обрабатываем ошибку
        document.getElementById('message').textContent = error.message;
    }
});

function goToRegistration() {
    window.location.href = '/registration';
}

function goToAccount() {
    window.location.href = '/account';
}

function goToAutomats(){
    window.location.href = '/automats'
}

function goToDocuments(){
    window.location.href = '/documents'
}