# SPDX-License-Identifier: GPL-3.0-only
"""Smoke-test the standalone loopback launcher without opening a browser."""
import subprocess
import sys
from pathlib import Path
import unittest
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]


class LauncherTest(unittest.TestCase):
    def test_standalone_server(self):
        proc = subprocess.Popen([sys.executable, str(ROOT / 'tools/pigeon_gui.py'), '--no-open', '--port', '0'],
                                cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            line = proc.stdout.readline().strip()
            self.assertTrue(line.startswith('Pigeon GUI: http://127.0.0.1:'), line)
            url = line.removeprefix('Pigeon GUI: ')
            for suffix, expected in (('', b'Pigeon'), ('app.js', b'import'), ('../', b'Open sample tool')):
                with urlopen(url + suffix, timeout=5) as response:
                    self.assertEqual(response.status, 200)
                    self.assertIn(expected, response.read())
        finally:
            proc.terminate()
            proc.communicate(timeout=5)


if __name__ == '__main__':
    unittest.main()
