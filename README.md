# shadeaid
small project to help with shading 


//TODO
```markdown
# Project To-Do List

## 1. Backend (Python)

### 1.1 Finalize the Project Structure
- ✅ Create the `src/app` and `src/tests` folders (already done).
- ✅ Add a `main.py` file for your backend entry point (already done).

### 1.2 Set Up Flask Backend
- [ ] Add a basic Flask API in `main.py` to test routes.
- [ ] Create a `/process-image` route that accepts an image file for processing.
- [ ] Add placeholder logic in `process.py` for converting an image to grayscale and identifying shading patterns.

### 1.3 Install Dependencies
- [✅] Add Python libraries to `requirements.txt`:
  - Flask
  - OpenCV (`opencv-python`)
  - Pillow
  - NumPy
  - Scikit-Image
- [✅] Install dependencies locally:
  ```bash
  pip install -r requirements.txt
  ```

### 1.4 Write Tests
- [ ] Write basic unit tests in `src/tests/test_app.py` to validate API functionality.
- [ ] Write tests for `process.py` to ensure the image processing logic works.

### 1.5 Run and Test Locally
- [ ] Start the Flask server:
  ```bash
  python src/app/main.py
  ```
- [ ] Test the API using a tool like Postman or cURL.

---

## 2. Frontend (Flutter)

### 2.1 Create and Set Up the Flutter Project
- ✅ Run `flutter create flutter_frontend` to initialize the project.
- ✅ Verify the default app runs successfully with `flutter run`.

### 2.2 Plan App Structure
- [ ] Organize the `lib/` directory:
  - Create directories for `screens`, `widgets`, and `services`.

### 2.3 Build UI
- [ ] Create a **Home Screen** with two main features:
  - Upload a reference image.
  - Display processed image results.
- [ ] Add an **Image Upload Screen**:
  - Use a package like `image_picker` to select images from the device.

### 2.4 Integrate with Backend
- [ ] Use the `http` package to make API calls to your Python backend.
- [ ] Set up a service file (e.g., `services/api_service.dart`) to handle the `/process-image` API endpoint.

---

## 3. Testing and Debugging

### 3.1 Debugging
- [ ] Debug the Flask backend for image processing and API requests.
- [ ] Debug the Flutter app for UI responsiveness and API integration.

### 3.2 Testing
- [ ] Write unit tests for Flutter using the `flutter_test` package.
- [ ] Test the full end-to-end workflow:
  1. Upload an image in the Flutter app.
  2. Send it to the backend for processing.
  3. Display the processed image with shading guides in the app.
```
