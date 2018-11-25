from core.motion.matrix import Matrix


def get_cavalera(l, angle=120):
    return Matrix([
        1, 0, 0, 0,
        0, 1, 0, 0,
        l*angle, l*angle, 0, 0,
        0, 0, 1, 0
    ])


def get_visible_faces(faces):
    return [i for i in faces if faces.isvisible()]