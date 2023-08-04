from pycatlib.category import *

# span is the category X <-l- A -r-> Y
span = Category(
    objects=["X", "A", "Y"],
    morphisms=["l", "r", "id_X", "id_A", "id_Y"],
    domain={"l": "A", "r": "A", "id_X": "X", "id_A": "A", "id_Y": "Y"},
    codomain={"l": "X", "r": "Y", "id_X": "X", "id_A": "A", "id_Y": "Y"},
    id={"X": "id_X", "A": "id_A", "Y": "id_Y"},
    composition={
        ("id_X", "id_X"): "id_X",
        ("id_X", "l"): "l",
        ("l", "id_A"): "l",
        ("id_A", "id_A"): "id_A",
        ("r", "id_A"): "r",
        ("id_Y", "r"): "r",
        ("id_Y", "id_Y"): "id_Y",
    }
)
cospan = span.op()

def test_span():
    # is not initial
    assert len(span.morphisms) != 0
    # is not terminal
    assert len(span.morphisms) != 1
    # is not discrete
    assert not span.is_discrete()
    # is not monoid
    assert len(span.objects) != 1
    # does not have terminal object
    assert not span.has_terminal_object()
    # has initial object
    assert cospan.has_terminal_object()
    # is preorder
    assert span.is_preorder()
    # is skeletal
    assert span.is_skeletal()
    # is connected
    assert span.is_connected()
    # has equalizers
    assert span.has_equalizers()
    # has coequalizers
    assert cospan.has_equalizers()
    # is not groupoid
    assert not span.is_groupoid()
    # has binary products
    assert span.has_binary_products()
    # does not have binary coproducts
    assert not cospan.has_binary_products()
    # does not have finite products
    assert not span.has_finite_products()
    # does not have finite coproducts
    assert not cospan.has_finite_products()
    # is not complete
    assert not span.is_finitely_complete()
    # is not cocomplete
    assert not cospan.is_finitely_complete()