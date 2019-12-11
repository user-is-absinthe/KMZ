import sys
import os
import traceback
import zipfile

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        msg = "Error parameters! Usage: python module.py <output filename> <input filename>"
        print(msg)
        raise Exception(msg)
    try:
        output_fname = sys.argv[1]
        input_filenames = sys.argv[2:]
        if os.path.exists(output_fname):
            os.remove(output_fname)
        
        result = [None] * len(input_filenames)
        
        # Processing ...
        for input_index, input_fname in enumerate(input_filenames):
            result[input_index] = (input_fname, open(input_fname).read()[::-1])
        #
        
        with zipfile.ZipFile(output_fname, 'w') as zip:
            for fname, data in result:
                with zip.open(fname, 'w') as result_file:
                    result_file.write(str(data).encode("utf-8"))
    except:
        print(traceback.format_exc())
        raise