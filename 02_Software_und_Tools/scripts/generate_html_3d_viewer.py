# -*- coding: utf-8 -*-
"""
Erzeugt den interaktiven 3D CAD Viewer mit echter 3D-Bemaßung (Dimension Lines, Masspfeile & CAD-Labels).
"""

import trimesh
import json
import os

mesh = trimesh.load(r'c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\bauteil_1001.stl')
verts = mesh.vertices.flatten().tolist()
faces = mesh.faces.flatten().tolist()

html_template = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Bauteil_1001 Flanschplatte - 3D CAD Masspruefung</title>
    <style>
        body { margin: 0; padding: 0; overflow: hidden; background: #121417; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #fff; }
        #canvas-container { width: 100vw; height: 100vh; display: block; }
        #ui-overlay {
            position: absolute; top: 16px; left: 16px;
            background: rgba(24, 27, 33, 0.92); backdrop-filter: blur(10px);
            padding: 18px 22px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.12);
            box-shadow: 0 12px 36px rgba(0,0,0,0.6); width: 330px; pointer-events: auto; z-index: 100;
        }
        h1 { margin: 0 0 4px 0; font-size: 18px; color: #38bdf8; font-weight: 600; }
        .subtitle { font-size: 12px; color: #94a3b8; margin-bottom: 12px; }
        .section-title { font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin: 10px 0 4px 0; font-weight: 700; }
        .spec-item { font-size: 12px; margin: 3px 0; display: flex; justify-content: space-between; }
        .spec-label { color: #94a3b8; }
        .spec-val { color: #f1f5f9; font-weight: 600; font-family: monospace; font-size: 12px; }
        .btn-group { margin-top: 14px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        button {
            background: #1e293b; border: 1px solid #334155; color: #e2e8f0;
            padding: 7px 10px; border-radius: 6px; font-size: 11px; font-weight: 500; cursor: pointer;
            transition: all 0.2s ease; text-align: center;
        }
        button:hover { background: #0284c7; border-color: #38bdf8; color: #fff; }
        button.active { background: #0284c7; border-color: #38bdf8; color: #fff; }
        #instructions {
            position: absolute; bottom: 16px; left: 50%; transform: translateX(-50%);
            background: rgba(15, 23, 42, 0.85); padding: 8px 20px; border-radius: 20px;
            font-size: 12px; color: #cbd5e1; pointer-events: none; border: 1px solid rgba(255,255,255,0.1);
        }
        .dim-badge {
            position: absolute; background: rgba(15, 23, 42, 0.85); color: #38bdf8;
            padding: 2px 7px; border-radius: 4px; font-size: 11px; font-weight: 600;
            font-family: monospace; border: 1px solid #0284c7; pointer-events: none;
            transform: translate(-50%, -50%); transition: opacity 0.2s; white-space: nowrap;
        }
    </style>
    <!-- Three.js + OrbitControls -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    <div id="ui-overlay">
        <h1>Bauteil_1001 Messprotokoll</h1>
        <div class="subtitle">Dipl.-Ing. Bujanovski CAD/CAM Inspektion</div>
        
        <div class="section-title">Ermittelte 3D-Masse</div>
        <div class="spec-item"><span class="spec-label">Laenge X:</span><span class="spec-val">80.00 mm</span></div>
        <div class="spec-item"><span class="spec-label">Breite Y:</span><span class="spec-val">50.00 mm</span></div>
        <div class="spec-item"><span class="spec-label">Dicke Z:</span><span class="spec-val">12.00 mm</span></div>
        <div class="spec-item"><span class="spec-label">Kreistasche:</span><span class="spec-val">&Oslash; 30.0 x 3.0 mm</span></div>
        <div class="spec-item"><span class="spec-label">4x Bohrung:</span><span class="spec-val">&Oslash; 6.0 mm (Z-12)</span></div>
        <div class="spec-item"><span class="spec-label">Bohrabstand X / Y:</span><span class="spec-val">60.0 / 30.0 mm</span></div>

        <div class="section-title">Physikalische Werte</div>
        <div class="spec-item"><span class="spec-label">Volumen (V):</span><span class="spec-val">44.53 cm&sup3;</span></div>
        <div class="spec-item"><span class="spec-label">Masse Alu (6082):</span><span class="spec-val" style="color:#4ade80;">120.24 g</span></div>
        <div class="spec-item"><span class="spec-label">Masse Stahl (S235):</span><span class="spec-val" style="color:#f59e0b;">349.58 g</span></div>

        <div class="btn-group">
            <button id="btn-dim" class="active" onclick="toggleDimensions()">3D-Bemaszung</button>
            <button onclick="toggleEdges()">CAD-Kanten</button>
            <button onclick="resetView('iso')">Isometrie</button>
            <button onclick="resetView('top')">Draufsicht (Z0)</button>
        </div>
    </div>

    <div id="instructions">
        Linksklick: Drehen | Mausrad: Zoomen | Rechtsklick: Verschieben
    </div>

    <div id="canvas-container"></div>
    <div id="labels-container"></div>

    <script>
        const verts = """ + json.dumps(verts) + """;
        const faces = """ + json.dumps(faces) + """;

        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xf1f5f9);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 1000);
        camera.position.set(80, 85, 80);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        document.getElementById('canvas-container').appendChild(renderer.domElement);

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.target.set(0, 0, 0);

        // Licht
        scene.add(new THREE.AmbientLight(0xffffff, 0.72));
        const dirLight = new THREE.DirectionalLight(0xffffff, 0.65);
        dirLight.position.set(60, 110, 80);
        dirLight.castShadow = true;
        scene.add(dirLight);

        const dirLight2 = new THREE.DirectionalLight(0x94a3b8, 0.35);
        dirLight2.position.set(-60, -40, -50);
        scene.add(dirLight2);

        // Boden-Gitter
        const grid = new THREE.GridHelper(160, 16, 0x94a3b8, 0xcbd5e1);
        grid.position.y = -6.01;
        scene.add(grid);

        // Koordinatensystem G54 Vorne-Links-Oben
        // x_3d = X - 40, y_3d = Z + 6, z_3d = -(Y - 25)
        // Vorne Links Oben ist X=0, Y=0, Z=0 -> x_3d=-40, y_3d=+6, z_3d=+25
        const axes = new THREE.AxesHelper(25);
        axes.position.set(-40, 6, 25);
        scene.add(axes);

        // Geometrie
        const geometry = new THREE.BufferGeometry();
        const posArr = new Float32Array(faces.length * 3);
        for(let i=0; i<faces.length; i++) {
            const vIdx = faces[i] * 3;
            posArr[i*3] = verts[vIdx] - 40;
            posArr[i*3+1] = verts[vIdx+2] + 6;
            posArr[i*3+2] = -(verts[vIdx+1] - 25);
        }
        geometry.setAttribute('position', new THREE.BufferAttribute(posArr, 3));
        geometry.computeVertexNormals();

        const material = new THREE.MeshStandardMaterial({
            color: 0x93c5fd,
            roughness: 0.32,
            metalness: 0.35
        });
        const mesh = new THREE.Mesh(geometry, material);
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        scene.add(mesh);

        // Schwarze CAD Kantenlinien
        const edgesGeo = new THREE.EdgesGeometry(geometry, 24);
        const edgesMat = new THREE.LineBasicMaterial({ color: 0x0f172a, linewidth: 2 });
        const edgeLines = new THREE.LineSegments(edgesGeo, edgesMat);
        mesh.add(edgeLines);

        // 3D-BEMAßUNGEN & MASSLINIEN
        const dimGroup = new THREE.Group();
        const dimMat = new THREE.LineBasicMaterial({ color: 0x0284c7, linewidth: 2 });
        const dimPointsMat = new THREE.PointsMaterial({ color: 0x0369a1, size: 4 });

        function createDimLine(p1, p2) {
            const geom = new THREE.BufferGeometry().setFromPoints([p1, p2]);
            return new THREE.Line(geom, dimMat);
        }

        // 1. Laenge 80 mm (entlang Frontkante, leicht nach vorne versetzt Z=+32)
        dimGroup.add(createDimLine(new THREE.Vector3(-40, 6, 32), new THREE.Vector3(40, 6, 32)));
        dimGroup.add(createDimLine(new THREE.Vector3(-40, 6, 25), new THREE.Vector3(-40, 6, 34))); // Hilfslinie links
        dimGroup.add(createDimLine(new THREE.Vector3(40, 6, 25), new THREE.Vector3(40, 6, 34)));   // Hilfslinie rechts

        // 2. Breite 50 mm (entlang rechter Kante, versetzt X=+48)
        dimGroup.add(createDimLine(new THREE.Vector3(48, 6, 25), new THREE.Vector3(48, 6, -25)));
        dimGroup.add(createDimLine(new THREE.Vector3(40, 6, 25), new THREE.Vector3(50, 6, 25)));  // Hilfslinie vorne
        dimGroup.add(createDimLine(new THREE.Vector3(40, 6, -25), new THREE.Vector3(50, 6, -25)));// Hilfslinie hinten

        // 3. Dicke 12 mm (vertikal an rechter vorderer Ecke)
        dimGroup.add(createDimLine(new THREE.Vector3(48, 6, 25), new THREE.Vector3(48, -6, 25)));
        dimGroup.add(createDimLine(new THREE.Vector3(40, -6, 25), new THREE.Vector3(50, -6, 25)));

        // 4. Kreistasche Durchmesser Ø30 mm
        dimGroup.add(createDimLine(new THREE.Vector3(-15, 6.2, 0), new THREE.Vector3(15, 6.2, 0)));

        scene.add(dimGroup);

        // 2D Text-Labels auf 3D projiziert
        const labelDefs = [
            { pos: new THREE.Vector3(0, 6, 34), text: "Länge = 80 mm" },
            { pos: new THREE.Vector3(51, 6, 0), text: "Breite = 50 mm" },
            { pos: new THREE.Vector3(51, 0, 25), text: "Dicke = 12 mm" },
            { pos: new THREE.Vector3(0, 7.5, 0), text: "Ø 30 mm x Tiefe 3 mm" },
            { pos: new THREE.Vector3(-30, 7.5, 15), text: "4x Bohrung Ø 6 mm" }
        ];

        const labelEls = labelDefs.map(d => {
            const el = document.createElement('div');
            el.className = 'dim-badge';
            el.innerText = d.text;
            document.getElementById('labels-container').appendChild(el);
            return { el, pos: d.pos };
        });

        function updateLabels() {
            if(!dimGroup.visible) {
                labelEls.forEach(l => l.el.style.opacity = '0');
                return;
            }
            labelEls.forEach(l => {
                const p = l.pos.clone().project(camera);
                if(p.z > 1) {
                    l.el.style.opacity = '0';
                    return;
                }
                const x = (p.x * 0.5 + 0.5) * window.innerWidth;
                const y = (-(p.y * 0.5) + 0.5) * window.innerHeight;
                l.el.style.left = `${x}px`;
                l.el.style.top = `${y}px`;
                l.el.style.opacity = '1';
            });
        }

        let dimVisible = true;
        function toggleDimensions() {
            dimVisible = !dimVisible;
            dimGroup.visible = dimVisible;
            document.getElementById('btn-dim').classList.toggle('active', dimVisible);
            updateLabels();
        }

        function toggleEdges() {
            edgeLines.visible = !edgeLines.visible;
        }

        function resetView(type) {
            if(type === 'iso') {
                camera.position.set(75, 80, 75);
                controls.target.set(0, 0, 0);
            } else if(type === 'top') {
                camera.position.set(0, 115, 0.001);
                controls.target.set(0, 0, 0);
            }
            controls.update();
        }

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            updateLabels();
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>"""

out_file = r'c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\flanschplatte_3d_viewer.html'
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(html_template)
print('Viewer mit 3D-Bemaszung aktualisiert:', out_file)
