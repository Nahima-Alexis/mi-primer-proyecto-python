# Git y GitHub - Apunte Completo

## 📚 Tabla de Contenidos
1. [Conceptos Básicos](#conceptos-básicos)
2. [Flujo de Trabajo](#flujo-de-trabajo)
3. [Comandos Esenciales](#comandos-esenciales)
4. [Paso a Paso Práctico](#paso-a-paso-práctico)
5. [Referencia Rápida](#referencia-rápida)

---

## 🎯 Conceptos Básicos

### Git
- **Sistema de control de versiones** = Sistema que guarda el historial de cambios de tu código
- Funciona **localmente** en tu computadora
- Permite volver a versiones anteriores si algo sale mal
- Permite que múltiples personas trabajen sin conflictos

### GitHub
- **Plataforma en la nube** para almacenar repositorios Git
- Es como Dropbox para código
- Permite colaboración y compartir código
- Portafolio profesional para mostrar tu trabajo

### Relación Git ↔ GitHub
```
TU COMPUTADORA          INTERNET               GITHUB
     ↓                    ↓                       ↓
  Git (local)     ←→  Conexión segura  ←→  Repositorio remoto
  Tu código            (comandos)            (en la nube)
```

---

## 🔄 Flujo de Trabajo Principal

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  1. Creas repositorio en GitHub                        │
│     └→ https://github.com/nuevo-repo                   │
│                                                         │
│  2. Clonas a tu compu (descargas)                      │
│     └→ git clone <URL>                                 │
│                                                         │
│  3. Editas archivos (escribes código)                  │
│     └→ Cambias archivos en tu editor                   │
│                                                         │
│  4. Guardas cambios con Commit                         │
│     └→ git add .                                        │
│     └→ git commit -m "Descripción"                     │
│                                                         │
│  5. Subes a GitHub (Push)                              │
│     └→ git push                                         │
│                                                         │
│  6. GitHub tiene tu código actualizado ✅              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 📖 Términos Clave

| Término | Significado | Ejemplo |
|---------|------------|---------|
| **Repository** | Carpeta de tu proyecto con todo el historial | `mi-primer-proyecto-python` |
| **Commit** | "Foto" de tus cambios en un momento | `"Agregué función de login"` |
| **Push** | Subir cambios a GitHub (compu → GitHub) | `git push` |
| **Pull** | Descargar cambios desde GitHub (GitHub → compu) | `git pull` |
| **Branch** | Versión paralela del proyecto | `main`, `nueva-feature` |
| **Clone** | Descargar un repositorio completo | `git clone <URL>` |
| **.gitignore** | Archivo que dice qué ignorar | Archivos temporales, pycache, etc |
| **README.md** | Documentación del proyecto | Descripción, instrucciones, autor |

---

## 💻 Comandos Esenciales

### Configuración Inicial (una sola vez)
```bash
# Configura tu nombre
git config --global user.name "Tu Nombre"

# Configura tu email
git config --global user.email "tu@email.com"

# Verifica que quedó bien
git config --global --list
```

### Clonar un Repositorio
```bash
# Descargar un repositorio desde GitHub
git clone https://github.com/usuario/nombre-repo.git

# Entrar en la carpeta
cd nombre-repo
```

### Ver Estado
```bash
# Muestra qué archivos cambiaron
git status
```

### Agregar y Hacer Commit
```bash
# Agrega TODOS los cambios
git add .

# Crea un commit con descripción
git commit -m "Descripción clara de qué hiciste"

# Ejemplo real:
git commit -m "Agregué función para calcular promedio"
```

### Subir a GitHub
```bash
# Sube tus commits a GitHub
git push
```

### Descargar Cambios desde GitHub
```bash
# Descarga cambios si alguien más actualizó el repo
git pull
```

### Ver Historial
```bash
# Muestra el historial de commits
git log

# Versión más legible
git log --oneline
```

---

## 📋 Paso a Paso Práctico

### Flujo Completo (lo que ya hiciste)

**1. Crear repositorio en GitHub:**
- Ve a github.com
- Click en **+** → **New repository**
- Llena: nombre, descripción
- Marca: **Add README file** y **Add .gitignore**
- Click **Create repository**

**2. Clonar a tu compu:**
```bash
cd Documentos
git clone https://github.com/TU_USUARIO/nombre-repo.git
cd nombre-repo
```

**3. Abrir en VS Code:**
```bash
code .
```

**4. Editar un archivo:**
- Abre cualquier archivo (ej: README.md)
- Modifica el contenido
- Guarda: `Ctrl + S`

**5. Ver qué cambió:**
```bash
git status
```

**6. Hacer commit:**
```bash
git add .
git commit -m "Actualicé el README"
```

**7. Subir a GitHub:**
```bash
git push
```

**8. Verificar en GitHub:**
- Ve a tu repositorio en github.com
- Actualiza la página
- ¡Verás tus cambios!

---

## 🚀 Referencia Rápida

### Comandos Más Usados
```bash
git status              # Ver cambios
git add .              # Agregar todos los cambios
git commit -m "msg"    # Hacer commit
git push               # Subir a GitHub
git pull               # Descargar cambios
git log --oneline      # Ver historial
```

### En VS Code (Alternativa a comandos)
1. Click en **Source Control** (rama en la izquierda)
2. Escribe mensaje en **Message**
3. Click **Commit**
4. Click **Sync** o **Publish Branch**

---

## ✅ Checklist para Empezar

- [ ] Git instalado (`git --version`)
- [ ] Cuenta GitHub creada
- [ ] VS Code instalado
- [ ] Extensión GitHub instalada en VS Code
- [ ] Git configurado con tu nombre y email
- [ ] Primer repositorio creado
- [ ] Primer commit hecho
- [ ] Primer push completado

---

## 📝 Notas Importantes

1. **Siempre escribe commits claros:** "Agregué login" es mejor que "cambios"
2. **Usa `.gitignore`:** No subas archivos innecesarios (pycache, .env, etc)
3. **Haz push regularmente:** No esperes a tener 100 cambios
4. **Lee el README:** Ese es tu "manual de instrucciones"
5. **Usa branches para nuevas features:** `main` siempre debe estar limpio

---

## 🎓 Próximos Pasos

1. Practica creando más repositorios
2. Aprende sobre **branches** (ramas paralelas)
3. Aprende sobre **Pull Requests** (para colaborar)
4. Practica con compañeros (hacer push/pull juntos)

¡Ya dominas lo básico! 🚀
