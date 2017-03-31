import chess
from tkinter import *
import chess.svg

def isPiece( pLetter):
    PieceLetters = ['K', 'Q', 'N', 'R', 'B']
    PieceLetterBlack = [ element.lower() for element in PieceLetters ]
    if pLetter in PieceLetters:
        return True
    if pLetter in PieceLetterBlack:
        return True
    return False

def GetPiece( pLetter, isBlack ):
    if ( isPiece(pLetter)):
        return chess.Piece.from_symbol(pLetter)
    if (isBlack):
        return chess.Piece.from_symbol('p')
    return chess.Piece.from_symbol('P')
    
def GetSquare( item ):
    item = item.upper()
    num1 = ord ( item[0] ) - ord ('A')
    num2 = ord ( item[1] )  - ord ('1')
    return num2 * 8 + num1  
          

def GetParsedBoard( positionString):
    board = chess.Board()
    board.clear()
    if ( positionString.lower().find('white')):
        board.turn = chess.WHITE
    else:
        board.turn = chess.BLACK
    positions = positionString.split(';')
    white_pos = positions[0]
    black_pos = positions[1]
    for item in white_pos.split(','):
        item  = item.strip()
        item  = item.upper()
        if ( isPiece(item[0]) and len(item) > 2 ):
            board.set_piece_at( GetSquare ( item[1:] ), GetPiece(item[0] , False) )
        else:
            board.set_piece_at( GetSquare ( item ), GetPiece('x' , False) )       
        print(len(item))
        print(item.strip())
    for item in black_pos.split(','):
        item = item.strip()  
        item = item.lower()
        if ( isPiece(item[0])  and len (item) > 2 ):
            board.set_piece_at( GetSquare ( item[1:] ), GetPiece (item[0], True))
        else:
            board.set_piece_at( GetSquare ( item ), GetPiece('x' , True) )
        print(len(item))
        print( item.strip())
    print( board )
    return board

class TrashGui:
    def __init__(self):
        self.root = Tk()
        self.root.title(' Chess Strings to Diagram Covertor ')
        self.textBox = Entry(self.root,width=100)
        self.textBox.pack(side = TOP,padx=5,pady=5)
        self.convertButton = Button(self.root, text=" Convert ",command=self.DumpFiles)
        self.convertButton.pack(side=TOP,padx=10,pady=10)
        self.index = 0; 
        mainloop()
    def DumpFiles(self):
        string = self.textBox.get()
        brd = GetParsedBoard(string)
        svg_content = chess.svg.board(brd)
        svgfile = open( "board" + str(self.index) + ".svg", "w")
        svgfile.write(svg_content)
        svgfile.close()
        fenfile = open("fen" + str(self.index) + ".txt" ,"w")
        fenfile.write(brd.fen())
        fenfile.close()
        self.index = self.index + 1 
        

if  __name__ == "__main__":
    gui = TrashGui()
