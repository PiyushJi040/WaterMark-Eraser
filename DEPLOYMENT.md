# 🚀 Deployment Guide

## Deploy to Render.com (FREE)

### Step-by-Step Instructions:

1. **Go to Render.com**
   - Visit: https://render.com
   - Click "Get Started for Free"
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" button
   - Select "Web Service"

3. **Connect Repository**
   - Select "Connect a repository"
   - Choose: `PiyushJi040/WaterMark-Eraser`
   - Click "Connect"

4. **Configure Service**
   - Name: `watermark-eraser`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Instance Type: `Free`

5. **Deploy**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Your app will be live at: `https://watermark-eraser.onrender.com`

### Alternative: PythonAnywhere (FREE)

1. **Sign Up**
   - Visit: https://www.pythonanywhere.com
   - Create free account

2. **Upload Code**
   - Go to "Files" tab
   - Upload all project files

3. **Install Dependencies**
   - Open Bash console
   - Run: `pip install --user -r requirements.txt`

4. **Configure Web App**
   - Go to "Web" tab
   - Add new web app
   - Choose Flask
   - Set source code path
   - Reload web app

5. **Access**
   - Your app: `https://yourusername.pythonanywhere.com`

## Notes:
- Render.com free tier sleeps after 15 min inactivity
- First request after sleep takes 30-60 seconds
- PythonAnywhere has daily CPU limits on free tier
