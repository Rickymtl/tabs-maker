from setuptools import setup


with open('requirements.txt') as f:
    required = f.read().splitlines()

entry_points = {
    'console_scripts': [
        'detect_onset = onset_detection:main',
    ],
}
setup(
    name='tabs-maker',
    version='0.0.1.dev',

    packages=[''],

    url='',
    license='FREE',
    author='mao',
    author_email='tianlemao98@gmail.com',
    description='Package for music transcription',
    install_requires=required,
    entry_points=entry_points
)
