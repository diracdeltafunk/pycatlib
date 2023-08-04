from .category import *

import os
import tempfile


class Functor:
    def __init__(
        self,
        domain: Category,
        codomain: Category,
        object_mapping: dict,
        morphism_mapping: dict,
        cache: dict = {},
    ):
        self.domain = domain
        self.codomain = codomain
        self.object_mapping = object_mapping
        self.morphism_mapping = morphism_mapping
        self.cache = cache

    def map_obj(self, o):
        return self.object_mapping.get(o)

    def map_mor(self, f):
        return self.morphism_mapping.get(f)

    def hom_mapping(self, x, y):
        return {f: self.morphism_mapping.get(f) for f in self.domain.hom(x, y)}

    def to_numbers(self):
        return Functor(
            domain=self.domain.to_numbers(),
            codomain=self.codomain.to_numbers(),
            object_mapping={
                self.domain.objects.index(o): self.codomain.objects.index(
                    self.map_obj(o)
                )
                for o in self.domain.objects
            },
            morphism_mapping={
                self.domain.morphisms.index(f): self.codomain.morphisms.index(
                    self.map_mor(f)
                )
                for f in self.domain.morphisms
            },
            cache={"is_numbers": True},
        )


def validate(fun: Functor) -> bool:
    d = fun.domain
    c = fun.codomain
    # Ensure domains & codomains are respected
    for f in d.morphisms:
        g = fun.map_mor(f)
        if c.dom(g) != fun.map_obj(d.dom(f)):
            return False
        if c.cod(g) != fun.map_obj(d.cod(f)):
            return False
    # Ensure ids are mapped to ids
    for o in d.objects:
        if fun.map_obj(d.i(o)) != c.i(fun.map_obj(o)):
            return False
    # Ensure composition is respected
    for (f, g), h in d.composition:
        if fun.map_mor(h) != c.comp(fun.map_mor(f), fun.map_mor(g)):
            return False
    return True


# # Generator of all functors from domain to codomain
# # TODO Implement without converting to numbers!
# def all_functors(domain: Category, codomain: Category):
#     domain = domain.to_numbers()
#     codomain = codomain.to_numbers()
#     with tempfile.NamedTemporaryFile("w") as minion_file:
#         minion_file.write("MINION 3\n")

#         minion_file.write("**VARIABLES**\n")
#         minion_file.write(
#             "DISCRETE mapping[{}] {{0..{}}}\n".format(
#                 len(domain.morphisms), len(codomain.morphisms) - 1
#             )
#         )

#         minion_file.write("**SHORTTUPLELIST**\n")
#         for (f, g), h in domain.composition.items():
#             rules_list = []
#             for (a, b), c in codomain.composition.items():
#                 rule = {(f, a), (g, b), (h, c)}
#                 if any(x[0] == y[0] and x[1] != y[1] for x in rule for y in rule):
#                     continue
#                 rules_list.append(list(rule))
#             minion_file.write("composition_{}_{} {}\n".format(f, g, len(rules_list)))
#             for rule in rules_list:
#                 minion_file.write("{}\n".format(rule))

#         minion_file.write("**CONSTRAINTS**\n")
#         # ids map to ids
#         for i in domain.objects:
#             minion_file.write(
#                 "ineq(mapping[{}], {}, -1)\n".format(i, len(codomain.objects))
#             )
#         # preserves composition
#         for f, g in domain.composition.keys():
#             minion_file.write("haggisgac(mapping,composition_{}_{})\n".format(f, g))

#         minion_file.write("**EOF**\n")

#         minion_file.flush()

#         with tempfile.NamedTemporaryFile("r") as out_file:
#             os.system(
#                 "minion -quiet -noprintsols -solsout {} -findallsols {} > /dev/null".format(
#                     out_file.name, minion_file.name
#                 )
#             )

#             for line in out_file:
#                 mapping = line.strip().split(" ")
#                 yield Functor(
#                     domain=domain,
#                     codomain=codomain,
#                     object_mapping={o: int(mapping[o]) for o in domain.objects},
#                     morphism_mapping={m: int(mapping[m]) for m in domain.morphisms},
#                 )


# # TODO Flesh out
# class NaturalTransformation:
#     def __init__(self, domain: Functor, codomain: Functor, mapping: dict):
#         self.domain = domain
#         self.codomain = codomain
#         self.mapping = mapping


# # Generator of all natural transformations from domain to codomain
# # TODO Implement without converting to numbers!
# def all_natural_transformations(domain: Functor, codomain: Functor):
#     domain = domain.to_numbers()
#     codomain = codomain.to_numbers()
#     domain_cat = domain.domain
#     codomain_cat = domain.codomain
#     with tempfile.NamedTemporaryFile("w") as minion_file:
#         minion_file.write("MINION 3\n")
#         minion_file.write("**VARIABLES**\n")
#         minion_file.write(
#             "DISCRETE mapping[{}] {{0..{}}}\n".format(
#                 len(domain_cat.objects), len(codomain_cat.morphisms) - 1
#             )
#         )

#         minion_file.write("**SHORTTUPLELIST**\n")
#         for f in domain_cat.morphisms:
#             possibilities = [
#                 (a, b)
#                 for a in codomain_cat.morphisms
#                 for b in codomain_cat.morphisms
#                 if codomain_cat.comp()
#             ]
#             # ! TODO FINISH
#         minion_file.write("**CONSTRAINTS**\n")
#         # ! TODO FINISH
#         minion_file.write("**EOF**\n")
#         minion_file.flush()

#         with tempfile.NamedTemporaryFile("r") as out_file:
#             os.system(
#                 "minion -quiet -noprintsols -solsout {} -findallsols {} > /dev/null".format(
#                     out_file.name, minion_file.name
#                 )
#             )

#             for line in out_file:
#                 mapping = line.strip().split(" ")
#                 # ! TODO FINISH
#     # ! TODO FINISH
