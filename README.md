# madpick
add .env file in main app at the same level of settings.py for environment variables
make a static folder madpick-main/static at the same level as manage.py
check node and npm using commands node -v npm -v
npm install tailwind @tailwindcss/cli
inside static create input.css
in the static/css/input.css add @import "tailwindcss";

make changes only in input.css

add "scripts" part inside package.json
"dependencies": {
    "@tailwindcss/cli": "^4.2.4",
    "tailwindcss": "^4.2.4"
  },
  "scripts":{
  "watch:css": "npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --watch",
  "build:css":"npx @tailwindcss/cli -i ./static/css/output.css -o ./static/css/output.min.css --minify"
  }

to watch changes locally~ npm run watch:css
-> static/css/output.css will be created which can run without production environment

to build for production~ npm run build:css
-> staticfiles/
-> staticfiles/css/output.min.css will be created which is a copy of static folder

summary::make changes to input.css then run ~npm run:watch then ~npm run:build
inside html link tag add<link rel="stylesheet" href="{% static 'output.min.css' %}">