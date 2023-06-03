import tkinter as tk

class ChessPiece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

class ChessBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Satranç")
        self.geometry("400x400")

        self.board = tk.Canvas(self, width=400, height=400)
        self.board.pack()

        self.create_board()

        self.pieces = self.initialize_pieces()

        self.draw_pieces()

        self.selected_piece = None
        self.board.bind("<Button-1>", self.handle_click)

    def create_board(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = "white"
                else:
                    color = "gray"
                self.board.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill=color)

    def initialize_pieces(self):
        pieces = []

        # Siyah taşlar
        pieces.append(ChessPiece("black", "rook"))
        pieces.append(ChessPiece("black", "knight"))
        pieces.append(ChessPiece("black", "bishop"))
        pieces.append(ChessPiece("black", "queen"))
        pieces.append(ChessPiece("black", "king"))
        pieces.append(ChessPiece("black", "bishop"))
        pieces.append(ChessPiece("black", "knight"))
        pieces.append(ChessPiece("black", "rook"))
        for i in range(8):
            pieces.append(ChessPiece("black", "pawn"))

        # Beyaz taşlar
        pieces.append(ChessPiece("white", "rook"))
        pieces.append(ChessPiece("white", "knight"))
        pieces.append(ChessPiece("white", "bishop"))
        pieces.append(ChessPiece("white", "queen"))
        pieces.append(ChessPiece("white", "king"))
        pieces.append(ChessPiece("white", "bishop"))
        pieces.append(ChessPiece("white", "knight"))
        pieces.append(ChessPiece("white", "rook"))
        for i in range(8):
            pieces.append(ChessPiece("white", "pawn"))

        return pieces

    def draw_pieces(self):
        for i in range(len(self.pieces)):
            piece = self.pieces[i]
            color = piece.color

            x = i % 8
            y = i // 8

            if piece.piece_type == "pawn":
                self.board.create_oval(x * 50 + 15, (7 - y) * 50 + 15, x * 50 + 35, (7 - y) * 50 + 35, fill=color, outline="black")
            elif piece.piece_type == "rook":
                self.board.create_rectangle(x * 50 + 10, (7 - y) * 50 + 10, x * 50 + 40, (7 - y) * 50 + 40, fill=color, outline="black")
            elif piece.piece_type == "knight":
                self.board.create_polygon(x * 50 + 25, (7 - y) * 50 + 10, x * 50 + 40, (7 - y) * 50 + 25, x * 50 + 35, (7 - y) * 50 + 40, x * 50 + 25, (7 - y) * 50 + 35, x * 50 + 15, (7 - y) * 50 + 40, x * 50 + 10, (7 - y) * 50 + 25, fill=color, outline="black")
            elif piece.piece_type == "bishop":
                self.board.create_polygon(x * 50 + 25, (7 - y) * 50 + 10, x * 50 + 40, (7 - y) * 50 + 10, x * 50 + 35, (7 - y) * 50 + 25, x * 50 + 40, (7 - y) * 50 + 40, x * 50 + 25, (7 - y) * 50 + 35, x * 50 + 10, (7 - y) * 50 + 40, x * 50 + 15, (7 - y) * 50 + 35, x * 50 + 10, (7 - y) * 50 + 25, fill=color, outline="black")
            elif piece.piece_type == "queen":
                self.board.create_polygon(x * 50 + 25, (7 - y) * 50 + 10, x * 50 + 40, (7 - y) * 50 + 10, x * 50 + 35, (7 - y) * 50 + 25, x * 50 + 40, (7 - y) * 50 + 40, x * 50 + 25, (7 - y) * 50 + 35, x * 50 + 10, (7 - y) * 50 + 40, x * 50 + 15, (7 - y) * 50 + 35, x * 50 + 10, (7 - y) * 50 + 25, fill=color, outline="black")
            elif piece.piece_type == "king":
                self.board.create_polygon(x * 50 + 25, (7 - y) * 50 + 10, x * 50 + 40, (7 - y) * 50 + 25, x * 50 + 35, (7 - y) * 50 + 40, x * 50 + 25, (7 - y) * 50 + 35, x * 50 + 15, (7 - y) * 50 + 40, x * 50 + 10, (7 - y) * 50 + 25, fill=color, outline="black")

    def handle_click(self, event):
        x = event.x // 50
        y = 7 - (event.y // 50)

        if self.selected_piece is None:
            for piece in self.pieces:
                if piece.piece_type == "pawn":
                    if piece.color == "white" and y == 1 or piece.color == "black" and y == 6:
                        if x == (i % 8):
                            self.selected_piece = piece
                            break
                else:
                    if x == (i % 8) and y == (i // 8):
                        self.selected_piece = piece
                        break
        else:
            # Burada taşın hareketini uygulayın ve güncellemeleri yapın
            pass

if __name__ == "__main__":
    app = ChessBoard()
    app.mainloop()
