from libreries import *

def define_subfolders(df: pd.DataFrame, class_names: dict, input_path: str, output_path: str,img_train_path: str, ds_img_path: str = 'path_img'):
    '''
    Objective: Create subfolder for each class within the training set folder

    args.
    ---
    df: pd.DataFrame; the training dataset

    class_names: dict; key define the class name and value refers to the integer label

    input_path: str; path where is the image set/ set
    
    output_path: str; path to send the image

    ret.
    ---
    None
    '''
    for k,v in class_names.items():
        image_list = list(df[df["label"]==v][ds_img_path])
        new_path_folder = img_train_path+"/"+output_path+"/"+k+"/"
        os.makedirs(new_path_folder, exist_ok=True)
        for i in image_list:
            image = i.split("/")[-1]
            old_path = img_train_path+"/"+output_path+"/"+image
            new_path = new_path_folder + image
            #print(k, old_path, "\n", new_path, "\n\n")
            shutil.copy(old_path, new_path)