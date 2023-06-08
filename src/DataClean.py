import os 
import shutil

def clean_static():
    rootdir_img = os.path.join(os.getcwd(),'static','images')
    dir_list_img = os.listdir(rootdir_img)
    
    rootdir_results = os.path.join(os.getcwd(),'static','results')
    
    dir_list_res = []
    for rootdir, dirs, files in os.walk(rootdir_results):
        for subdir in dirs:
            dir_list_res.append(os.path.join(rootdir, subdir))
    
    if len(dir_list_img)>=5:
        N = len(dir_list_img)
        sub_list = dir_list_img[N-2:]
        for img in sub_list:
            try:
                os.remove(os.path.join(os.getcwd(),'static','images',img))
            except OSError as e :
                print(e)
            
    if len(dir_list_res)>=5:
        N = len(dir_list_res)
        sub_list = dir_list_res[N-2:]
        
        for dir in sub_list:
            try:
                shutil.rmtree(dir)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
        

if __name__=="__main__":
    clean_static()