# Kurulan Uzantılar

- robocorp.robotframework-lsp
- robocorp.robocorp-code

# Yeni Robot Örnek Uygulaması Oluşturmak
1. Boş bir dizin yaratıp, VS Code ile açalım. 
2. Ctrl+Shift+P ile `Robocorp: Create Robot` komutu çalıştırılarak yeni projenin dosyaları şablondan oluşturulur
3. `conda.yaml` Dosyasına istenilen python paketleri eklenir:
```yaml
channels:
  # Define conda channels here.
  - conda-forge

dependencies:
  # Define conda packages here.
  # If available, always prefer the conda version of a package, installation will be faster and more efficient.
  # https://anaconda.org/search
  - python=3.7.5
  - pip=20.1
  - pip:
      # Define pip packages here.
      # https://pypi.org/
      - rpaframework==12.8.2 # https://rpaframework.org/releasenotes.html
      - pyshark # bu paketi ekledik
```
4. Kütüphane dizini farklı bir dizin olacaksa robot.yaml içinde `PYTHONPATH` dizinine eklenir
```yaml
tasks:
  Run all tasks:
    shell: python -m robot --report NONE --outputdir output --logtitle "Task log" tasks.robot

condaConfigFile: conda.yaml
artifactsDir: output
PATH:
  - .
PYTHONPATH:
  - .
  - kutuphane
ignoreFiles:
  - .gitignore
```
5. Kod değişiklikleri yapıldıktan sonra Ctrl+Shift+P kısayoluyla açılan komut giriş kutusuna `Robocorp:Run Robot` komutu girilir.

# Template: Standard Robot Framework

Want to get started using [Robot Framework](https://robocorp.com/docs/languages-and-frameworks/robot-framework/basics) this is the simplest template to start from.

This template robot:

- Uses [Robot Framework](https://robocorp.com/docs/languages-and-frameworks/robot-framework/basics) syntax.
- Includes all the necessary dependencies and initialization commands (`conda.yaml`).
- Provides a simple task template to start from (`tasks.robot`).

## Learning materials

- [All docs related to Robot Framework](https://robocorp.com/docs/languages-and-frameworks/robot-framework)
