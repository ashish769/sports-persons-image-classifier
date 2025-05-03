def classify_image(image_base_64_data,file_path=None):
    pass

def get_b64_test_image_for_messi():
    with open('b64.txt') as f:
        return f.read()
if __name__=="__main__":
    print(classify_image(get_b64_test_image_for_messi(),None))
