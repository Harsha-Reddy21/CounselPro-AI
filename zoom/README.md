# Zoom API Integration Setup Guide

This guide will help you set up a Zoom Server-to-Server OAuth app and configure your Python script to use it.

## Step 1: Create a Zoom Server-to-Server OAuth App

1. Log in to the [Zoom App Marketplace](https://marketplace.zoom.us/)
2. Click on "Develop" in the top-right corner
3. Select "Build App"
4. Choose "Server-to-Server OAuth" app type
5. Fill in the app name (e.g., "CounselPro Integration")
6. Click "Create"

## Step 2: Configure the App

1. Fill in the required information:
   - App Name
   - Company Name
   - Developer Contact Information
   
2. In the "App Credentials" section:
   - Note down the Account ID, Client ID, and Client Secret
   
3. Add the required scopes:
   - Click on "Scopes"
   - Add the necessary permissions your app needs (e.g., meeting:read, recording:read)
   
4. Activate your app by clicking "Activate"

## Step 3: Set Up Environment Variables

1. Create a `.env` file in the zoom directory with the following content:
```
ZOOM_ACCOUNT_ID=your_account_id_here
ZOOM_CLIENT_ID=your_client_id_here
ZOOM_CLIENT_SECRET=your_client_secret_here
```

2. Replace the placeholder values with the actual credentials from your Zoom app

## Step 4: Run the Script

```
python main.py
```

If configured correctly, you should receive an access token that you can use for other Zoom API calls.

## Troubleshooting

If you receive an `invalid_client` error:
- Double-check that your credentials are correct
- Ensure your app is activated
- Verify that you've added the necessary scopes
- Make sure you're using the correct account ID that owns the app
