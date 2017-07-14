import cairo
import pytest


def test_font_face_cmp_hash():
    surface = cairo.ImageSurface(0, 10, 10)
    context = cairo.Context(surface)
    ff = context.get_font_face()
    other = context.get_font_face()
    assert ff == other
    assert not ff != other
    assert hash(ff) == hash(other)

    sf = context.get_scaled_font()
    other = context.get_scaled_font()
    assert sf == other
    assert not sf != other
    assert hash(sf) == hash(other)

    fo = context.get_font_options()
    # FontOptions compare by their content and they are mutable, so not
    # hashable.
    with pytest.raises(TypeError):
        hash(fo)


def test_toy_font_get_slant():
    font_face = cairo.ToyFontFace("")
    assert font_face.get_slant() == cairo.FontSlant.NORMAL
    assert isinstance(font_face.get_slant(), cairo.FontSlant)


def test_toy_font_get_weight():
    font_face = cairo.ToyFontFace("")
    assert font_face.get_weight() == cairo.FontWeight.NORMAL
    assert isinstance(font_face.get_weight(), cairo.FontWeight)


@pytest.fixture
def font_options():
    surface = cairo.ImageSurface(0, 10, 10)
    return surface.get_font_options()


def test_font_options_get_antialias(font_options):
    assert font_options.get_antialias() == cairo.Antialias.DEFAULT
    assert isinstance(font_options.get_antialias(), cairo.Antialias)


def test_font_options_get_hint_metrics(font_options):
    assert font_options.get_hint_metrics() == cairo.HintMetrics.ON
    assert isinstance(font_options.get_hint_metrics(), cairo.HintMetrics)


def test_font_options_get_hint_style(font_options):
    assert font_options.get_hint_style() == cairo.HintStyle.DEFAULT
    assert isinstance(font_options.get_hint_style(), cairo.HintStyle)


def test_font_options_get_subpixel_order(font_options):
    assert font_options.get_subpixel_order() == cairo.SubpixelOrder.DEFAULT
    assert isinstance(font_options.get_subpixel_order(), cairo.SubpixelOrder)
