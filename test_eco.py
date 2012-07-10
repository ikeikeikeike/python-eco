try:
    from StringIO import StringIO
except ImportError:
    try:
        import StringIO
    except ImportError:
        from io import StringIO
import six
import eco
import execjs


def test_compile():
    assert eco.compile("Hello <%= @name %>")


def test_compile_with_io():
    io_ = StringIO("Hello <%= @name %>")
    assert eco.compile("Hello <%= @name %>") == eco.compile(io_)


def test_compilation_error():
    try:
        eco.compile("<%= foo")
    except execjs.ProgramError:
        pass


def test_context_for():
    context = eco.context_for("Hello <%= @name %>")
    assert "Hello " == context.call("render")
    assert "Hello Sam" == context.call("render", {"name": "Sam"})


def test_render():
    assert "Hello " == eco.render("Hello <%= @name %>")
    assert "Hello Sam" == eco.render("Hello <%= @name %>", name="Sam")
    assert six.u("Hello « Rémi »") == eco.render(six.u("Hello « <%= @name %> »"), name=six.u("Rémi"))


def test_runtime_error():
    context = eco.context_for("Hello <% throw 'foo' %>")
    try:
        context.call("render")
    except execjs.ProgramError:
        pass
