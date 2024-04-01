    def visit_Mul(self, node):
        """Обробляємо множення."""
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        """Обробляємо ділення."""
        right = self.visit(node.right)
        if right == 0:
            raise Exception("Ділення на нуль.")
        return self.visit(node.left) / right
