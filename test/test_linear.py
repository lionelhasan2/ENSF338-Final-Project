import sys
from pathlib import Path
from io import StringIO
import pytest


parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from myLib.datastructures.Nodes.DNode import DNode
from myLib.datastructures.Linear.SLL import SLL
from myLib.datastructures.Linear.DLL import DLL
from myLib.datastructures.Linear.CSLL import CSLL
from myLib.datastructures.Linear.CDLL import CDLL
from myLib.datastructures.Linear.LLStack import LLStack
from myLib.datastructures.Linear.LLQueue import LLQueue

from io import StringIO
import sys

def test_SLL_ConstructorsandInserters():
    print("Testing no node constructor, InsertTail, InsertHead, Insert, Print")
    captured_output = StringIO()
    sys.stdout = captured_output
    testsll = SLL()
    testsll.InsertTail(DNode(3))
    testsll.InsertHead( DNode(6))
    testsll.Insert(DNode(2), 2)
    testsll.InsertHead(DNode(2))
    testsll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 4\nSorted: No\nList content: 2 6 2 3 \n"

def test_SLL_Sort():
    testsll = SLL()
    testsll.InsertTail(DNode(3))
    testsll.InsertHead( DNode(6))
    testsll.Insert(DNode(2), 2)
    testsll.InsertHead(DNode(2))
    print("Testing sort and print")
    captured_output = StringIO()
    sys.stdout = captured_output
    testsll.Sort()
    testsll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 4\nSorted: Yes\nList content: 2 2 3 6 \n"

def test_SLL_SortInsert():
    testsll = SLL()
    testsll.InsertTail(DNode(3))
    testsll.InsertHead( DNode(6))
    testsll.Insert(DNode(2), 2)
    testsll.InsertHead(DNode(2))
    print("Testing sortInsert and print")
    captured_output = StringIO()
    sys.stdout = captured_output
    testsll.SortedInsert(DNode(5))
    testsll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 5\nSorted: Yes\nList content: 2 2 3 5 6 \n"

def test_SLL_Delete():
    testsll = SLL()
    testsll.InsertTail(DNode(3))
    testsll.InsertHead( DNode(6))
    testsll.Insert(DNode(2), 2)
    testsll.InsertHead(DNode(2))
    print("Testing deleteHead, deleteTail, delete")
    captured_output = StringIO()
    sys.stdout = captured_output
    testsll.DeleteHead()
    testsll.DeleteTail()
    testsll.Delete(DNode(2)) #DOESNT WORK RN
    testsll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 1\nSorted: Yes\nList content: 6 \n"

def test_SLL_Search():
    testsll = SLL()
    testsll.InsertTail(DNode(3))
    testsll.InsertHead( DNode(6))
    testsll.Insert(DNode(2), 2)
    print("Testing search")
    if(testsll.Search(DNode(2))): #THIS DOES NOT WORK
        print("Search function for the node with value 2  was successful")
        print(testsll.Search(DNode(2)))
    else:
        print("Search function for the node with value 2  was unsuccessful")
    print()
    
def test_SLL_Clear():
    print("Testing clear")
    testsll = SLL()
    testsll.InsertTail(DNode(3))
    testsll.InsertHead( DNode(6))
    testsll.Insert(DNode(2), 2)
    captured_output = StringIO()
    sys.stdout = captured_output
    testsll.Clear()
    testsll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 0\nSorted: Yes\nList content: \n"

def test_DLL_ConstructorsandInserters():
    print("Testing no node constructor, InsertTail, InsertHead, Insert, Print")
    captured_output = StringIO()
    sys.stdout = captured_output
    dll =DLL(DNode(0)) 
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    dll.Insert(DNode(6), 1)
    dll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 5\nSorted: False\nList content: 6 -5 6 0 3 \n"

def test_DLL_Sort():
    dll = DLL(DNode(0)) 
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    dll.Insert(DNode(6), 1)
    print("Testing sort and print")
    captured_output = StringIO()
    sys.stdout = captured_output
    dll.Sort()
    dll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 5\nSorted: True\nList content: -5 0 3 6 6 \n"

def test_DLL_SortInsert():
    dll = DLL(DNode(0)) 
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    dll.Insert(DNode(6), 1)
    print("Testing sortInsert and print")
    captured_output = StringIO()
    sys.stdout = captured_output
    dll.SortedInsert(DNode(-1))
    dll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 6\nSorted: True\nList content: -5 -1 0 3 6 6 \n"

def test_DLL_Delete():
    dll = DLL(DNode(0)) 
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    dll.Insert(DNode(6), 1)
    print("Testing deleteHead, deleteTail, delete")
    captured_output = StringIO()
    sys.stdout = captured_output
    dll.DeleteHead()
    dll.DeleteTail()
    dll.Delete(DNode(6)) 
    dll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 2\nSorted: True\nList content: -5 0 \n"

def test_DLL_Search():
    dll = DLL(DNode(0)) 
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    print("Testing search")
    if(dll.Search(DNode(0))):
        print("Search function for the node with value 0  was successful")
        print(dll.Search(DNode(0)))
    else:
        print("Search function for the node with value 0  was unsuccessful")
    print()
    
def test_DLL_Clear():
    print("Testing clear")
    dll = DLL(DNode(0)) 
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    captured_output = StringIO()
    sys.stdout = captured_output
    dll.Clear()
    dll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 0\nSorted: Yes\nList content: \n"

def test_CSLL_ConstructorsandInserters():
    print("Testing no node constructor, InsertTail, InsertHead, Insert, Print")
    captured_output = StringIO()
    sys.stdout = captured_output
    csll = CSLL(DNode(2)) 
    csll.InsertHead(DNode(-5))
    csll.InsertTail(DNode(10))
    csll.Insert(DNode(10), 1)
    csll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 4\nSorted: No\nList content: 10 -5 2 10 \n"

def test_CSLL_Sort():
    csll = CSLL(DNode(2)) 
    csll.InsertHead(DNode(-5))
    csll.InsertTail(DNode(10))
    csll.Insert(DNode(10), 1)
    print("Testing sort and print")
    captured_output = StringIO()
    sys.stdout = captured_output
    csll.Sort()
    csll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 4\nSorted: Yes\nList content: -5 2 10 10 \n"

def test_CSLL_SortInsert():
    csll = CSLL(DNode(2)) 
    csll.InsertHead(DNode(-5))
    csll.InsertTail(DNode(10))
    csll.Insert(DNode(10), 1)
    print("Testing sortInsert and print")
    captured_output = StringIO()
    sys.stdout = captured_output
    csll.SortedInsert(DNode(-100))
    csll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 5\nSorted: Yes\nList content: -100 -5 2 10 10 \n"

def test_CSLL_Delete():
    csll = CSLL(DNode(2)) 
    csll.InsertHead(DNode(-5))
    csll.InsertTail(DNode(10))
    csll.Insert(DNode(10), 1)
    csll.SortedInsert(DNode(-100))
    print("Testing deleteHead, deleteTail, delete")
    captured_output = StringIO()
    sys.stdout = captured_output
    csll.DeleteHead()
    csll.DeleteTail()
    csll.Delete(DNode(10)) 
    csll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 2\nSorted: Yes\nList content: -5 2 \n"

def test_CSLL_Search():
    csll = CSLL() 
    csll.InsertHead(DNode(-5))
    csll.InsertTail(DNode(10))
    csll.Insert(DNode(10), 1)
    print("Testing search")
    if(csll.Search(DNode(-5))): #NGL IDK IF ITS SUPPOSED TO RETURN OBJECT OR SUCCESSFUL
        print("Search function for the node with value 0  was successful")
        print(csll.Search(DNode(-5)))
    else:
        print("Search function for the node with value 0  was unsuccessful")
    print()
    
def test_CSLL_Clear():
    print("Testing clear")
    csll = CSLL(DNode(0)) 
    csll.InsertHead(DNode(-5))
    csll.Insert(DNode(6), 2)
    captured_output = StringIO()
    sys.stdout = captured_output
    csll.Clear()
    csll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 0\nSorted: Yes\nList content: \n"

def test_CDLL_ConstructorsandInserters():
    print("Testing no node constructor, InsertTail, InsertHead, Insert, Print")
    captured_output = StringIO()
    sys.stdout = captured_output
    cdll = CDLL(DNode(0))
    cdll.InsertHead(DNode(-5))
    cdll.Insert(DNode(5), 2)
    cdll.InsertTail(DNode(3))
    cdll.Insert(DNode(6), 2)
    cdll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List Length: 5\nSorted Status: False\nList Content: -5 6 5 0 3 \n"

def test_CDLL_Sort():
    cdll = CDLL(DNode(0))
    cdll.InsertHead(DNode(-5))
    cdll.Insert(DNode(5), 2)
    cdll.InsertTail(DNode(3))
    cdll.Insert(DNode(6), 2)
    print("Testing sort and print")
    captured_output = StringIO()
    sys.stdout = captured_output
    cdll.Sort()
    cdll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List Length: 5\nSorted Status: True\nList Content: -5 0 3 5 6 \n"

def test_CDLL_SortInsert():
    cdll = CDLL(DNode(0))
    cdll.InsertHead(DNode(-5))
    cdll.Insert(DNode(5), 2)
    cdll.InsertTail(DNode(3))
    cdll.Insert(DNode(6), 2)
    print("Testing sortInsert and print")
    captured_output = StringIO()
    sys.stdout = captured_output
    cdll.SortedInsert(DNode(-100))
    cdll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List Length: 6\nSorted Status: True\nList Content: -100 -5 0 3 5 6 \n"

def test_CDLL_Delete():
    cdll = CDLL(DNode(0))
    cdll.InsertHead(DNode(-5))
    cdll.Insert(DNode(5), 2)
    cdll.InsertTail(DNode(3))
    cdll.Insert(DNode(6), 2)
    cdll.SortedInsert(DNode(-100))
    print("Testing deleteHead, deleteTail, delete")
    captured_output = StringIO()
    sys.stdout = captured_output
    cdll.DeleteHead()
    cdll.DeleteTail()
    cdll.Delete(DNode(6)) 
    cdll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List Length: 4\nSorted Status: True\nList Content: -5 0 3 5 \n"

def test_CDLL_Search():
    cdll = CDLL(DNode(0)) 
    cdll.Insert(DNode(6), 2)
    cdll.InsertTail(DNode(3))
    print("Testing search")
    if(cdll.Search(DNode(0))):
        print("Search function for the node with value 0  was successful")
        print(cdll.Search(DNode(0)))
    else:
        print("Search function for the node with value 0  was unsuccessful")
    print()
    
def test_CDLL_Clear():
    print("Testing clear")
    cdll = CDLL(DNode(0)) 
    cdll.InsertHead(DNode(-5))
    cdll.Insert(DNode(6), 2)
    captured_output = StringIO()
    sys.stdout = captured_output
    cdll.Clear()
    cdll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 0\nSorted: Yes\nList content: \n"

def test_LLStack_ConstructorAndPush():
    captured_output = StringIO()
    sys.stdout = captured_output
    stack = LLStack(DNode(0)) 
    stack.Push(DNode(-5))
    stack.Push(DNode(3))
    stack.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 3\nSorted: No\nList content: 3 -5 0 \n"

def test_LLStack_Delete():
    stack = LLStack(DNode(0)) 
    stack.Push(DNode(-5))
    stack.Push(DNode(3))
    print("Testing deleteHead, deleteTail, delete")
    captured_output = StringIO()
    sys.stdout = captured_output
    stack.DeleteHead() #calls stack.pop
    temp = stack.Pop()
    stack.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert temp == (-5)
    assert output == "List size: 1\nSorted: Yes\nList content: 0 \n"

def test_LLStack_Search():
    stack = LLStack(DNode(0)) 
    stack.Push(DNode(-5))
    stack.Push(DNode(3))
    print("Testing search")
    if(stack.Search(DNode(0))):
        print("Search function for the node with value 0  was successful")
        print(stack.Search(DNode(0)))
    else:
        print("Search function for the node with value 0  was unsuccessful")
    print()
    
def test_LLStack_Clear():
    stack = LLStack(DNode(0)) 
    stack.Push(DNode(-5))
    captured_output = StringIO()
    sys.stdout = captured_output
    stack.Clear()
    stack.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 0\nSorted: Yes\nList content: \n"

def test_LLQueueEnqueDequeueClear():
    testLLQueue = LLQueue()
    testLLQueue.enqueue(DNode(3))
    testLLQueue.enqueue(DNode(6))
    testLLQueue.enqueue(DNode(2))

    captured_output = StringIO()
    sys.stdout = captured_output
    testLLQueue.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == "List size: 3\nSorted: No\nList content: 3 6 2 \n"

    testLLQueue.enqueue(DNode(1))
    testLLQueue.enqueue(DNode(5))
    testLLQueue.enqueue(DNode(9))
    testLLQueue.enqueue(DNode(12))
    dequeueNodeVal = testLLQueue.dequeue()


    captured_output = StringIO()
    sys.stdout = captured_output
    testLLQueue.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == 'List size: 7\nSorted: No\nList content: 6 2 1 5 9 12 \n'
    assert dequeueNodeVal == 3

    testLLQueue.Clear()
    captured_output = StringIO()
    sys.stdout = captured_output
    testLLQueue.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == 'List size: 0\nSorted: Yes\nList content: \n'

if __name__ == "__main__":
    print("TESTING SLL \n")
    test_SLL_ConstructorsandInserters()
    test_SLL_Sort()
    test_SLL_SortInsert()
    test_SLL_Delete()
    test_SLL_Search()
    test_SLL_Clear()

    print("TESTING DLL \n")
    test_DLL_ConstructorsandInserters()
    test_DLL_Sort()
    test_DLL_SortInsert()
    test_DLL_Delete()
    test_DLL_Search()
    test_DLL_Clear()

    print("TESTING CSLL \n")
    test_CSLL_ConstructorsandInserters()
    test_CSLL_Sort()
    test_CSLL_SortInsert()
    test_CSLL_Delete()
    test_CSLL_Search()
    test_CSLL_Clear()

    print("TESTING CDLL \n")
    test_CDLL_ConstructorsandInserters()
    test_CDLL_Sort()
    test_CDLL_SortInsert()
    test_CDLL_Delete()
    test_CDLL_Search()
    test_CDLL_Clear()

    print("TESTING LLStack \n")
    test_LLStack_ConstructorAndPush()
    test_LLStack_Delete()
    test_LLStack_Search()
    test_LLStack_Clear()

    print("TESTING LLQueue \n")
    test_LLQueueEnqueDequeueClear()
    

