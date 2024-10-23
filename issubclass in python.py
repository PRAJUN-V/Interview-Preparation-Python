class A:
    pass
class B:
    pass
class C(A, B):
    pass

print(issubclass(B, A))
print(issubclass(C, B))
