import face_recognition
from PIL import Image, UnidentifiedImageError
import os

def is_supported_format(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()  # Verify that it is a valid image
        return True
    except (IOError, SyntaxError, UnidentifiedImageError):
        return False

def find_person_image(target_image_path, group_images_folder, output_folder):
    # Load the target image
    target_image = face_recognition.load_image_file(target_image_path)
    target_face_encodings = face_recognition.face_encodings(target_image)
    
    print(f"Number of faces detected in target image: {len(target_face_encodings)}")

    if not target_face_encodings:
        print(f"No faces found in target image: {target_image_path}")
        return
    
    target_face_encoding = target_face_encodings[0]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_name in os.listdir(group_images_folder):
        image_path = os.path.join(group_images_folder, image_name)

        if not is_supported_format(image_path):
            print(f"Skipping unsupported image format: {image_name}")
            continue

        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        
        print(f"Number of faces detected in {image_name}: {len(face_encodings)}")

        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([target_face_encoding], face_encoding)
            if match[0]:
                pil_image = Image.open(image_path)
                pil_image.save(os.path.join(output_folder, image_name))
                break
