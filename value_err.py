# https://stackoverflow.com/questions/72418911/getting-valueerror/72419171#72419171
import argparse

def isArmstrong(val: int) -> bool:
    """
    The :param val: will be tested to see if its an Armstrong number.

    Arguments:
        val {int} -- positive integer only.
    Returns:
        bool -- true is /false isn't
    """
 
    # break the int into its respective digits
    parts = [int(i) for i in str(val)]
 
    # begin test.
    counter = 0
    for part in parts:
        counter += part**3
    return (counter == val)
 
 
if __name__ == "__main__":
    description = 'Test if a number is an Armstrong number.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('val', type=int, help='The number to test.')
    args = parser.parse_args()
    
    if isArmstrong(args.val):
        print("true")
    else:
        print("false")
