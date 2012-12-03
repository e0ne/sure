## #!/usr/bin/env python
# -*- coding: utf-8 -*-
# <sure - assertion toolbox>
# Copyright (C) <2010-2012>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sure


def test_it_works_with_objects():
    ("anything that inherits from object should be patched")

    (4).should.equal(2 + 2)
    "foo".should.equal("f" + ("o" * 2))
    {}.should.be.empty


# TODO
# def test_it_works_with_non_objects():
#     (u"anything that inherits from non-object should also be patched")

#     class Foo:
#         pass

#     f = Foo()

#     f.should.be.a(Foo)
