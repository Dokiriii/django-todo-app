from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Меняем текст подсказок на русский
        self.fields['username'].help_text = 'Не более 150 символов. Буквы, цифры и символы @/./+/-/_'
        
        self.fields['password1'].help_text = '''
            <ul class="password-requirements">
                <li>Пароль не должен быть слишком похож на другую личную информацию</li>
                <li>Пароль должен содержать минимум 8 символов</li>
                <li>Пароль не должен быть слишком простым</li>
                <li>Пароль не может состоять только из цифр</li>
            </ul>
        '''
        
        self.fields['password2'].help_text = 'Введите тот же пароль, что и выше'
        
        # Меняем метки полей
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Дополнительная проверка на кириллицу (если хочешь)
        return username