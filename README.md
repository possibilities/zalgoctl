# zalgoctl

A Zalgo text generator CLI.

## Usage

```bash
# Basic encoding
./zalgoctl "Hello World"

# With style preset
./zalgoctl "He comes" --style heavy

# Pipe text
echo "Fear me" | ./zalgoctl --intensity 20

# Decode (strip combining marks)
./zalgoctl decode "Z̷a̸l̵g̶o̷"

# Analyze text
./zalgoctl analyze "Z̷a̸l̵g̶o̷"
```

## Options

- `--style` - Preset: whisper, subtle, moderate, heavy, extreme, demonic, void
- `--intensity` - Set all directions at once (0-100)
- `--up/--mid/--down` - Control mark placement
- `--pattern` - Distribution: wave, fade-in, fade-out, pulse, crescendo, spike
- `--seed` - Reproducible output
- `--prob` - Probability each character gets corrupted (0.0-1.0)

Run `./zalgoctl --help` for all options.
