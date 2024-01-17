# Step 1: Use the official Node.js base image
FROM node:latest

# Step 2: Set the working directory
WORKDIR /usr/src/app

# Step 3: Copy application files
COPY . .

# Step 4: Install dependencies
# Uncomment the next line if you have a package.json file
# RUN npm install

# Step 5: Expose the port your app runs on
# Replace 3000 with your application's port if it's different
EXPOSE 3000

# Step 6: Start the application
CMD ["node", "server.js"]