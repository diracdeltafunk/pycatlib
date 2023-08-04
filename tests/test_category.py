from pycatlib.category import *

from itertools import permutations

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
    },
)
cospan = span.op()

# the group S3
s3 = Category(
    objects=[0],
    morphisms=list(permutations(range(3), 3)),
    domain={f: 0 for f in permutations(range(3), 3)},
    codomain={f: 0 for f in permutations(range(3), 3)},
    id={0: (0, 1, 2)},
    composition={
        (f, g): (f[g[0]], f[g[1]], f[g[2]])
        for f in permutations(range(3), 3)
        for g in permutations(range(3), 3)
    },
)
s3_op = s3.op()


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


def test_s3():
    # is not initial
    assert len(s3.morphisms) != 0
    # is not terminal
    assert len(s3.morphisms) != 1
    # is not discrete
    assert not s3.is_discrete()
    # is monoid
    assert len(s3.objects) == 1
    # does not have terminal object
    assert not s3.has_terminal_object()
    # does not have initial object
    assert not s3_op.has_terminal_object()
    # is not preorder
    assert not s3.is_preorder()
    # is skeletal
    assert s3.is_skeletal()
    # is connected
    assert s3.is_connected()
    # is groupoid
    assert s3.is_groupoid()
    # does not have equalizers
    assert not s3.has_equalizers()
    # does not have coequalizers
    assert not s3_op.has_equalizers()
    # does not have binary products
    assert not s3.has_binary_products()
    # does not have binary coproducts
    assert not s3_op.has_binary_products()
    # does not have finite products
    assert not s3.has_finite_products()
    # does not have finite coproducts
    assert not s3_op.has_finite_products()
    # is not complete
    assert not s3.is_finitely_complete()
    # is not cocomplete
    assert not s3_op.is_finitely_complete()
