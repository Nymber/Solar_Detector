# 🏠 Solar Houses Detection System

A streamlined solar panel detection system that focuses on finding houses with existing solar panels and generates property data with high-resolution house images for any location.

## 🎯 Goals

Generate a CSV file with:
- **Owner Names** - Property owner information
- **Addresses** - Complete property addresses  
- **House Images** - High-resolution aerial photos
- **Solar Data** - Existing solar installations and potential analysis

## 🚀 Quick Start

1. **Create virtual environment:**
   ```bash
   python3 -m venv solar_env
   source solar_env/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get Google Maps API key:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the  Solar API
   - Create an API key

4. **Run the system:**
   ```bash
   python3 run_solar_houses.py
   ```

## 📊 Output

The system generates:
- **`solar_houses_summary.csv`** - Main export with owner names, addresses, images, and solar data
- **`house_images/`** - High-resolution satellite photos
- **`interactive_map.html`** - Visual map of properties with solar status
- **`reports/`** - Analysis reports

## 🔧 Files

- **`solar_houses_detector.py`** - Main detection system
- **`run_solar_houses.py`** - Simple runner script
- **`config.py`** - Configuration settings
- **`requirements.txt`** - Dependencies
- **`.gitignore`** - Git ignore file for environment and output files

## 📋 CSV Output Format

| Column | Description |
|--------|-------------|
| `property_id` | Unique property identifier |
| `owner_name` | Property owner name |
| `address` | Complete property address |
| `house_image_path` | Path to house image file |
| `has_solar_panels` | Boolean: has existing solar panels |
| `estimated_panel_count` | Estimated number of panels |
| `system_size_kw` | Solar system size in kW |
| `installation_year` | Year solar was installed |
| `solar_potential_score` | Solar potential score (0-100) |
| `roi_percentage` | Return on investment percentage |

## 🌍 Supported Locations

- **St. Tammany Parish, LA** (default)
- **New Orleans, LA**
- **Baton Rouge, LA**
- **Any custom location** (will generate generic data)

## 🎮 Usage Examples

```bash
# Interactive mode
python3 run_solar_houses.py

# Command line mode
python3 solar_houses_detector.py --api-key YOUR_KEY --location "New Orleans, LA" --max-properties 15
```

---

*Built for detecting houses with existing solar panels and analyzing solar potential*
