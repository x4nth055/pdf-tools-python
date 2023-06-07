import os
import sys
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet

# Get your own API key from https://dev.apryse.com/get-key
API_KEY = "<YOUR_API_KEY>"

# initiate PDFNet
PDFNet.Initialize(API_KEY)

def get_size_format(b, factor=1024, suffix="B"):
    """Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'"""
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def compress_file(input_file: str, output_file: str):
    """Compress the file at input_file and output to output_file
    Args:
        input_file (str): Input PDF file
        output_file (str): Output PDF file"""
    if not output_file:
        # Name the output file the same as input file + '_compressed.pdf' if no output_file name provided
        output_file = os.path.splitext(input_file)[0] + "_compressed.pdf"
    try:
        # Create a PDFDoc to read the PDF file
        doc = PDFDoc(input_file)
        # Optimize the PDF with the default settings
        doc.InitSecurityHandler()
        # Reduce PDF size by removing redundant information and compressing data streams
        Optimizer.Optimize(doc)
        # Save the Optimized document to the output file
        doc.Save(output_file, SDFDoc.e_linearized)
        doc.Close()
    except Exception as e:
        print(f"Error: {str(e)}")
        doc.Close()
        return False
    # Get the file size of input and output file
    compressed_size = os.path.getsize(output_file)
    original_size = os.path.getsize(input_file)
    # Calculate the compression ratio
    compression_ratio = 1 - (compressed_size / original_size)
    # Print info
    print(f"Input file & size: {input_file}, {get_size_format(original_size)}")
    print(f"Output file & size: {output_file}, {get_size_format(compressed_size)}")
    print(f"Saved {compression_ratio:.2%} space")
    return True


if __name__ == "__main__":
    # Get the input and output file names from the command line
    input_file = sys.argv[1]
    try:
        output_file = sys.argv[2]
    except IndexError:
        output_file = None
    compress_file(input_file, output_file)